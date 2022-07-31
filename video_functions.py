import threading
import pytube as tube
import datetime as dt



url = "https://youtu.be/8UVNT4wvIGY"



class VideoFunctions(tube.YouTube):

    #Time format for calculating the time 
    TIME_FORMAT = "%H:%M:%S"

    def __init__(self):
         self.TIME_FORMAT = '%H:%M:%S'



    #============ Functions ============

    #thread function to run each function in thread so the GUI doesnt get stuck

    @staticmethod
    def thread_function(function, arguments):

        function_in_thread = threading.Thread(target=function, args=arguments)

        function_in_thread.start()


    #networkSpeed function -> divides the filesize with the time taken for download

    @staticmethod
    def networkSpeed(filesize : int, time_took : int):
        try:
            size_in_mb = filesize/1000000
        except ZeroDivisionError:
            print("Filesize cant be zero!")
            return

        speed = int(size_in_mb/time_took)
        return speed


    #timeTaken function -> gets the times for the start and end the download function and subtracts them

    @staticmethod
    def timeTaken(start_time, end_time, in_seconds = True):
        difference_in_time = str(end_time - start_time)

        time_components = difference_in_time.split(':')

        if in_seconds:
            hours = int(time_components[0]) * 60 * 60
            minutes = int(time_components[1]) * 60
            seconds = hours + minutes + int(time_components[2])
            total_seconds = hours + minutes + seconds
            
            return total_seconds
        
        else:
            return time_components


    #fromSeconds function -> To convert seconds to hour:minute:seconds format
    @staticmethod
    def fromSeconds(sec : int):
        time_list = str(dt.timedelta(seconds=sec))
        time_list = time_list.split(":")

        modified_list = []
        for times in time_list:
            if int(times) == 0:
                pass
            else:
                modified_list.append(times)
        
        return ":".join(modified_list)
    

    #fromBytes function -> To convert bytes to better datasize(MB, GB, TB, etc.)
    @staticmethod
    def fromBytes(bytes : int):
        pass


    #createTime function -> for creating a time object at start and end of the download function

    def createTime(self):
        _time = dt.datetime.now()

        time_string = _time.strftime(self.TIME_FORMAT)
        formatted_time = dt.datetime.strptime(time_string, self.TIME_FORMAT)

        return formatted_time


    #downloadVideo function -> the name explains it, c'mon

    def downloadVideo(self, *args, **kwargs):
        started_on = self.createTime()

        yt_object = tube.YouTube(*args, **kwargs)

        video = yt_object.streams.get_highest_resolution()
        

        video.download()

        ended_on = self.createTime()

        time_taken = self.timeTaken(started_on, ended_on)
        speed_was = round(self.networkSpeed(video.filesize, time_taken), 4)

        print(f" Seconds took : {time_taken}")
        print(f" Average Speed : {speed_was}")




    #for getting the video data

    def getAllData(self, url):
        data_dict = {}

        video = tube.YouTube(url)

        data_dict['title'] = video.title
        data_dict['duration'] = self.fromSeconds(video.length)
        data_dict['views'] = video.views
        data_dict['size'] = round(video.streams.get_highest_resolution().filesize_approx/1000000, 1)
        data_dict['thumbnail-url'] = video.thumbnail_url

        return data_dict


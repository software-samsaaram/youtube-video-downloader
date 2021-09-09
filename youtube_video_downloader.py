'''
    File name: youtube_video_downloader.py
    Author: Software Samsaaram
    Date created: 10/09/2021
    Date last modified: 10/09/2021
    Python Version: 3.9.0
    Description: This python program downloads the YouTube video by taking the YouTube video URL as input
'''
from pytube import YouTube
import requests
import os

video_url = input("\nEnter the URL (Link) of the YouTube Video to download: ")      #Get the Input of the YouTube Video URL

if video_url:                                                                       #Check whether the user has given some input or not
    try:
        check_url = requests.get(video_url)                                         #Check if the URL is valid
        if check_url.status_code == 200:
            try:                                                                    #Check if the URL is of a YouTube Video
                yt = YouTube(video_url)
                video_title = yt.title
                views = yt.views
                duration = yt.length
                print("\nVideo Details:")
                print("    Title: ", video_title)
                print("    Views: ", views)
                print("    Duration: ", duration, "Seconds")
                videos = yt.streams                                                 #Get all the Streams of the Video
                video = list(enumerate(videos))
                print("\nThis video is available in following Format and Resolution combinations:\n")
                for i in video:                                                     #Loop through each of the available Streams of the Video to display
                    i = list(i)
                    details = str(i[1])
                    file_format = details.split()[2].split("=")[1].strip("\"")
                    file_resolution = details.split()[3].split("=")[1].strip("\"")
                    print(f"    {i[0] + 1}. Format: {file_format} Resolution: {file_resolution}")
                while True:                                                         #Ask the user to select option from the menu till he selects right input or selects to exit
                    file_index = input("\nChoose the File Format and Resolution combination from the above Menu(Enter x to exit): ")
                    if file_index.isdigit():
                        file_index = int(file_index)
                        if file_index >= 1 and file_index <= len(video):
                            dn_video = videos[(file_index - 1)]
                            print("\nPlease wait while the file is being downloaded !!")
                            dn_video.download()                                     #Download the Video
                            print(f"Download Completed. Video has been saved in the folder: {os.getcwd()}") #Show Download completed message and display the path in which the Video has been saved
                            break
                        else:
                            print(f"Please choose a number between 1 and {len(video)} or enter x to exit")
                    elif file_index == "x":
                        break
                    else:
                        print(f"Please choose a number between 1 and {len(video)} or enter x to exit")
            except Exception as e:
                print(f"\nError occured while attempting to download the video from URL '{video_url}'.\nError Message: {e}\nPossible Reason: This might not be a YouTube video URL or the video might have been deleted")
        else:
            print("Unable to connect to the URL. Please check the URL.")
    except Exception as e:
        print(f"\nError occured while trying to connecto the URL '{video_url}'.\nError Message: {e}")
else:
    print("\nNo Link received as Input. You need to enter the URL (Link) of the Video to download !")

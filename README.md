# video-afatyga
EC500 C1 Alex Fatyga <br>

# Main Exercise
Using the twitter feed, construct a daily video summarizing a twitter handle day <br>
- Convert text into an image in a frame
- Do a sequence of all texts and images in chronological order.
- Display each video frame for 3 seconds 
<br> <br>
This is completed in twitterHW2.py (using HW2's twitter API assignment) <br>
getMsg(username) - takes in an input username and returns a list of tuples of text or a url and a 0 or 1 to signify whether the first of the tuple is a string of the tweet or a url of the image associated <br>
saveAsFile(textOrUrl, boolVal, count) - takes in a string, a 1 or 0 to indicate whether the first argument is tweet or a url and a count to know what to save the file as. Each image is saved as "tweets" count# ".png".  <br>
imageThreads(listOfLinks, count) - creates threads to run saveAsFile, each thread is an image to be created, the function iterates through listOfLinks to create the thread and returns a list of threads. count is the starting number for the filenames and increments count while iterating through listOfLinks to always assign a different filename. This starting number is important so that with multiporcessing there aren't processes using the same files when creating the video. <br>
createVideo(num) - this function creates the video by using a subprocess. num specifies which process is running and is multiplied by 100 (as with the count in each filename). This value multiplied by 100 is the starting number for when creating the video from images. For example, a starting number of 100 means the video will be created from images saved as tweets100.png and upwards. <br>

# Task 1 
Task 1 is located in ./task1/ <br>
I tested the code provided in Python Threads vs Processes and saw that CPU bound was faster than IO bound.

# Rest of Assignment
Establish a processing criteria: <br>
- How many API calls you can handle simultaneously and why?
- For example, run different API calls at the same time?
- Split the processing of an API into multiple threads?
- Include tracking interface to show how many processes are going on and success of 

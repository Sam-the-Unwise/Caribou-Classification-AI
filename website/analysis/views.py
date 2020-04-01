from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResultForm
from django.contrib import messages
from .models import Result
import os
import re
from random import choice

videoID = ""
videoPath = ""

def showContent(request):
    db = Result.objects.all()
    return render(request, 'analysis/demo-content.html', {"list": db})

def SearchContent(request):
    db = Result.objects.all()
    return render(request, 'analysis/demo-content.html', {"list": db})

def googleForm(request):
    return render(request, 'analysis/googleForm.html')

@login_required
def classification(request):
    return render(request, 'analysis/classification.html')

@login_required
def category(request):
    global videoID
    global videoPath
    targetDb = []
    db = Result.objects.all()
    if request.method == 'POST':
        Video_Quality = request.POST.getlist('Quality', '')
        # get queries that satisfy users' selection
        if Video_Quality:
            for filedElement in Video_Quality:
                targetData=db.filter(Video_Quality=filedElement)
                if targetData is not None:
                    targetDb.extend(targetData)
                    # print(targetDb)

            # get those videos id
            videoList = []
            for key in targetDb:
                # if key == 'File_Name':
                videoList.append(key.pk)
                # print(key.pk)
                # print(videoList)
            videoID = choice(videoList)
            videoPath = "/videos/" + videoID + ".mp4"
            return render(request, 'analysis/targetVideo.html', {'videoPath': videoPath, 'videoID': videoID})
            # example for demo
            # return render(request, 'analysis/demo-content.html', {"list": targetDb})
    return render(request, 'analysis/category.html')

@login_required
def targetVideo(request):
    global videoID
    global videoPath
    videoID = getRandVideoID()
    videoPath = "/videos/" + videoID + ".mp4"
    return render(request, 'analysis/targetVideo.html', {'videoPath': videoPath, 'videoID': videoID})

# 当前使用的
@login_required
def ResultPrefilled(request, video_id):
    searchQuery = Result.objects.filter(File_Name=video_id)
    # if the query exists
    if searchQuery.exists():
        result = Result.objects.get(File_Name=video_id)
        prefilledName = {'Observer_Name': request.user.first_name + ' ' + request.user.last_name}
        if request.method == "POST":
            form = ResultForm(instance=result, data=request.POST, initial=prefilledName)
            if form.is_valid():
                form.save()
                messages.success(request, f'Analysis for video:{video_id} has been submitted successfully!')
                return redirect('analysis-category')
        else:
            form = ResultForm(instance=result, initial=prefilledName)
    # otherwise, create a new query
    else:
        prefilledName = {
            'File_Name': videoID,
            'Observer_Name': request.user.first_name + ' ' + request.user.last_name}
        if request.method == "POST":
            form = ResultForm(data=request.POST, initial=prefilledName)
            if form.is_valid():
                form.save()
                return redirect('analysis-category')
        else:
            form = ResultForm(initial=prefilledName)
    return render(request, 'analysis/classification.html', {'form': form, 'videoPath': videoPath, 'videoID': videoID})



# -------Used functions-------
def getRandVideoID():
    pwd = os.getcwd()
    video_Path = pwd+'\\analysis\\static\\videos'
    fileList=getAllFile(video_Path)
    # randomly choose one video
    randomVideo = choice(fileList)
    return randomVideo

def getAllFile( path ):
    # initialize list to store path and name of all files
    allPath = []
    #  get the list of all files and directories in the specified directory
    fileList = os.listdir( path )
    for eachFile in fileList:
        videoName = re.search(r'(.+?)\.', eachFile).group(1)
        # append file names to the list
        allPath.append(videoName)
    return allPath




import xlrd 
import shutil
from os import path
import os

VIDEO_QUALITY = 7
VIDEO_TITLE = 0

# skip all the videos before this number
VIDEO_NUMBER_THAT_VIDEO_CATEG_WAS_CHANGED_AT = 2543

# set paths that videos will be obtained from and saved to
UNSORTED_VIDEO_PATH = "./unsorted_videos/"
SORTED_VIDEO_PATH = "./sort_videos/"


def access_excel(file_name):
    # Program extracting all columns 
    wb = xlrd.open_workbook(file_name) 
    sheet = wb.sheet_by_index(0) 
    
    # For row 0 and column 0 
    sheet.cell_value(0, 0) 
    
    for i in range(sheet.nrows): 
        if(i > VIDEO_NUMBER_THAT_VIDEO_CATEG_WAS_CHANGED_AT):
            
            this_videos_quality = sheet.cell_value(i, VIDEO_QUALITY)
            this_videos_name = sheet.cell_value(i, VIDEO_TITLE) + ".mp4"

            if(this_videos_quality == "EXCELLENT"):
                if(path.exists(UNSORTED_VIDEO_PATH + this_videos_name)):
                    shutil.move(UNSORTED_VIDEO_PATH + this_videos_name, SORTED_VIDEO_PATH + "Excellent/" + this_videos_name)

            elif(this_videos_quality == "FAIR to GOOD"):
                if(path.exists(UNSORTED_VIDEO_PATH + this_videos_name)):
                    shutil.move(UNSORTED_VIDEO_PATH + this_videos_name, SORTED_VIDEO_PATH + "Good_to_Fair/" + this_videos_name)

            elif(this_videos_quality == "POOR"):
                if(path.exists(UNSORTED_VIDEO_PATH + this_videos_name)):
                    shutil.move(UNSORTED_VIDEO_PATH + this_videos_name, SORTED_VIDEO_PATH + "Poor/" + this_videos_name)

            elif(this_videos_quality == "EXTREMELY OBSTRUCTED"):
                if(path.exists(UNSORTED_VIDEO_PATH + this_videos_name)):
                    shutil.move(UNSORTED_VIDEO_PATH + this_videos_name, SORTED_VIDEO_PATH + "Extremely_Obstructed/" + this_videos_name)

            else:
                print("Have not obtained this video or information about this video")
                




access_excel("Caribou_data.xlsx")
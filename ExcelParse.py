#imports the ability to read from an excel file
import xlrd
import os
import pathlib

FILE_NAME = 0
DATE = 2
QUALITY = 7

EXCELLENT = 1
GOOD = 2
POOR = 3
EO = 4

NONE = 0

originalPath = os.getcwd()
#the location of the excel file
direc = originalPath+"/ExcelSheet/CaribouVideoProcessing_10899Responses_20191210.xlsx"

workbook = xlrd.open_workbook(direc)
sheet = workbook.sheet_by_index(FILE_NAME)

#file name is column 0
#date is column 2
#quality is column 7


maxRows = sheet.nrows

row = 1

EXCEL_DATE_IN_NUMBER = 43557.40

def greaterThanOrEqualToExpectedDay( date, comparedDate ):
    if( comparedDate >= date ):
        return 1
    return NONE

def dateFromString( date ):
    global EXCEL_DATE_IN_NUMBER
    return greaterThanOrEqualToExpectedDay( EXCEL_DATE_IN_NUMBER, date )

def getVidQuality( row ):
    global sheet
    vidQual = sheet.cell_value( row, QUALITY )
    return vidQual

def selectFolder( videoQuality ):
    quality = videoQuality.lower()
    if( quality == 'excellent'):
        return EXCELLENT
    elif( quality == "good" or quality == "fair to good" or quality == "good to fair"):
        return GOOD
    elif( quality == "poor to fair" or quality == "poor"):
        return POOR
    elif( quality == "extremely obstructed"):
        return EO
    else:
        return NONE
    
def checkFileExists( file ):
    os.chdir(originalPath+'/VideosBeforeSort/UnsortedVideos/')
    boolean = os.path.isfile( file )
    os.chdir(originalPath)
    return boolean

def moveFileToFolder( file, quality ):
    currentDir = "/VideosBeforeSort/UnsortedVideos/" + file
    moveToDir = ""
    #path = str(pathlib.Path().absolute())
    if( quality == EXCELLENT ):
        moveToDir = "/VideosBeforeSort/SortedVideos/Excellent/" + file
    elif( quality == GOOD ):
        moveToDir = "/VideosBeforeSort/SortedVideos/Good_to_Fair/" + file
    elif( quality == POOR ):
        moveToDir = "/VideosBeforeSort/SortedVideos/Poor/" + file
    elif( quality == EO ):
        moveToDir = "/VideosBeforeSort/SortedVideos/ExtremelyObstructed/" + file
    else:
        return 0

    print( "moving " + title + " to " + originalPath + moveToDir + "\n")
    os.replace(originalPath+currentDir, originalPath+moveToDir)

count = 0

while( row < maxRows ):
    
    path = pathlib.Path().absolute()
    date = sheet.cell_value(row, DATE)

    if( dateFromString( date ) == 1 ):
        title = sheet.cell_value( row, FILE_NAME )
        title = title + ".mp4"
        videoQuality = getVidQuality( row )
        if( checkFileExists( title ) ):
            count += 1
            
            moveFileToFolder( title, selectFolder( videoQuality ))

    row+=1
    
print(str(count) + " videos were successfully sorted into their correct folders")
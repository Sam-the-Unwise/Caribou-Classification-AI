#imports the ability to read from an excel file
import xlrd
import os
import pathlib

originalPath = os.getcwd()
#the location of the excel file
direc = originalPath+"\ExcelSheet\CaribouVideoProcessing_10899Responses_20191210.xlsx"

workbook = xlrd.open_workbook(direc)
sheet = workbook.sheet_by_index(0)


#file name is column 0
#date is column 2
#quality is column 7

maxRows = sheet.nrows

row = 1

EXCEL_DATE_IN_NUMBER = 43557.40

def greaterThanOrEqualToExpectedDay( date, comparedDate ):
    if( comparedDate >= date ):
        return 1
    return 0

def dateFromString( date ):
    global EXCEL_DATE_IN_NUMBER
    return greaterThanOrEqualToExpectedDay( EXCEL_DATE_IN_NUMBER, date )

def getVidQuality( row ):
    global sheet
    vidQual = sheet.cell_value( row, 7 )
    return vidQual

    
def checkFileExists( file ):
    os.chdir(originalPath+'/Downloads')
    boolean = os.path.isfile( file )
    os.chdir(originalPath)
    return boolean

def moveFileToFolder( file, quality ):
    currentDir = "/Downloads/"+file
    moveToDir = ""
    #path = str(pathlib.Path().absolute())
    if( quality == 1 ):
        moveToDir = "/VideosBeforeSort/Excellent/"+file
    elif( quality == 2 ):
        moveToDir = "/VideosBeforeSort/Good_to_Fair/"+file
    elif( quality == 3 ):
        moveToDir = "/VideosBeforeSort/Poor/"+file
    elif( quality == 4 ):
        moveToDir = "/VideosBeforeSort/ExtremelyObstructed/"+file
    else:
        return 0
    os.replace(originalPath+currentDir, originalPath+moveToDir)
    

while( row < maxRows ):
    
    path = pathlib.Path().absolute()
    date = sheet.cell_value(row,2)

    if( dateFromString( date ) == 1 ):
        title = sheet.cell_value( row, 0 )
        title = title + ".mp4"
        videoQuality = getVidQuality( row )
        if( checkFileExists( title ) ):
            print( "moving " + title + "\n")
            
            moveFileToFolder( title, videoQuality)

    row+=1
    

import os, zipfile
import variables

dir_name = "../VideosBeforeSort/"
output_folder = variables.UNSORTED_VIDEO_INPUT_PATH

extension = ".zip"

os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(output_folder)
        zip_ref.close()
        #os.remove(file_name)
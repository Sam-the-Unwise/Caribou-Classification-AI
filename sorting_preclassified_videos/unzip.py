import os, zipfile

dir_name = "/media/sam-the-unwise/Sentient Toaster/Caribou"
output_folder = "/media/sam-the-unwise/Sentient Toaster/Caribou/Videos"
extension = ".zip"

os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(output_folder)
        zip_ref.close()
        #os.remove(file_name)
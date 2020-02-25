#!/usr/bin/env python
import os, shutil


TEST_EXCELLENT_FRAME_PATH = "../dataset/testing_set_frames/Excellent/"

# decalre variables and paths
INPUT_PATH_TRAINING = "../dataset/training_set/"
INPUT_PATH_VALIDATION = "../dataset/validation_set/"

OUTPUT_PATH_TRAINING = "../dataset/training_set_frames/"
OUTPUT_PATH_VALIDATION = "../dataset/validation_set_frames/"

PATH_EXCELLENT = "Excellent/"
PATH_GOOD = "Good_to_fair/"
PATH_POOR = "Poor/"
PATH_EXTREMELY_OBSTRUCTED = "Extremely_Obstructed/"


def deleteFramesInFolder(folderPath):
	file_list = os.listdir(folderPath)

	for filename in file_list:
		file_path = os.path.join(folderPath, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
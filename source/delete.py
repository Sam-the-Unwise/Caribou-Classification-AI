#!/usr/bin/env python
import os, shutil
import variables


###############################################################################
# FUNCTION NAME: deleteFramesInFolder
# WHAT IT DOES: function that will loop through the provided folder path and 
#			delete all the frames
# RETURN: none
###############################################################################

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

###############################################################################
# FUNCTION NAME: deleteTrainAndVal
# WHAT IT DOES: function that will pass in all the folder paths that need their
#			frames deleted
# RETURN: none
###############################################################################

def deleteTrainAndVal():
	# delete all excellent #
	deleteFramesInFolder(variables.OUTPUT_TRAINING_PATH + variables.EXCELLENT_FOLDER)
	deleteFramesInFolder(variables.OUTPUT_VALIDATION_PATH + variables.EXCELLENT_FOLDER)

	# delete all extremely obstructed #
	deleteFramesInFolder(variables.OUTPUT_TRAINING_PATH + variables.EXTREMELY_OBSTRUCTED_FOLDER)
	deleteFramesInFolder(variables.OUTPUT_VALIDATION_PATH + variables.EXTREMELY_OBSTRUCTED_FOLDER)

	# delete all good #
	deleteFramesInFolder(variables.OUTPUT_TRAINING_PATH + variables.GOOD_FOLDER)
	deleteFramesInFolder(variables.OUTPUT_VALIDATION_PATH + variables.GOOD_FOLDER)
		
	# delete all poor #
	deleteFramesInFolder(variables.OUTPUT_TRAINING_PATH + variables.POOR_FOLDER)
	deleteFramesInFolder(variables.OUTPUT_VALIDATION_PATH + variables.POOR_FOLDER)

	
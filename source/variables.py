###############################################################################
# AUTHOR: Samantha
#
# DESCRIPTION: file that will hold all the necessary variables used throughout
#       all the different files
#
# VERSION: 1.0.0
###############################################################################

# PATHS FOR SORTING VIDEOS
SORTING_VIDEOS_INPUT_PATH = "../VideosBeforeSort/SortedVideos/"
SORTING_VIDEOS_OUTPUT_PATH = INPUT_TRAINING_PATH

# decalre variables and paths
INPUT_TRAINING_PATH = "../dataset/training_set/"
INPUT_VALIDATION_PATH = "../dataset/validation_set/"

OUTPUT_TRAINING_PATH = "../dataset/training_set_frames/"
OUTPUT_VALIDATION_PATH = "../dataset/validation_set_frames/"

EXCELLENT_FOLDER = "Excellent/"
EXTREMELY_OBSTRUCTED_FOLDER = "Extremely_Obstructed/"
GOOD_FOLDER = "Good_to_fair/"
POOR_FOLDER = "Poor/"

MODEL_PATH = './models/model.h5'
MODEL_WEIGHTS_PATH = './models/weights.h5'
TEST_PATH = "./dataset/testing_set"


VIDEO_OUTPUT_PATH = "../dataset/output/"

# other variables
EXPECTED_FRAMES = 18

EXCELLENT_CAT_NUMBER = 0
EXTREMELY_OBSTRUCTED_CAT_NUMBER = 1
GOOD_CAT_NUMBER = 2
POOR_CAT_NUMBER = 3

# file to create a split in each of our data categorise for both training and validation purposes
# split should be as follows:   
#       60% of videos into training
#       20% of videos into validation
#       20% of videos into testing

import os
from os import path

FROM_FILE_PATH_STARTER = "././sorting_preclassified_videos/sorted_videos/"
FROM_FILE_PATH_STARTER_UNCLASSIFIED = "././sorting_preclassified_videos/unsorted_videos/"
TO_FILE_PATH_TRAIN_START = "././dataset/training_set/"
TO_FILE_PATH_VAL_START = "././dataset/validation_set/"
TO_FILE_PATH_TEST_START = "././dataset/testing_set/"


# NOTE:
    # since we have a large amount of unknown videos, this file will simply find the amount of videos 
    #       used to create the validation set and use the same amount in the test set for our first few
    #       trials
    # later, once accuracy has achieved a high-enough amount, all videos will be moved into test set

def split_for_testing_and_validation(from_file_path, to_file_path_train, to_file_path_val):
    print("Training and Validation Sets Completed")

def move_videos_to_testing(from_file_path, to_file_path_test, amount_of_videos):
    print("Testing Set completed")



# sort EXCELLENT videos
number_of_excellent_validation_videos = split_for_testing_and_validation(FROM_FILE_PATH_STARTER + "Excellent/", 
                                                                        TO_FILE_PATH_TRAIN_START + "Excellent/", 
                                                                        TO_FILE_PATH_VAL_START + "Excellent/")

move_videos_to_testing(FROM_FILE_PATH_STARTER_UNCLASSIFIED, 
                        TO_FILE_PATH_TEST_START, 
                        number_of_excellent_validation_videos)


# sort EXTREMELY_OBSTRUCTED videos
number_of_extremely_obstructed_validation_videos = split_for_testing_and_validation(FROM_FILE_PATH_STARTER + "Extremely_Obstructed/", 
                                                                        TO_FILE_PATH_TRAIN_START + "Extremely_Obstructed/", 
                                                                        TO_FILE_PATH_VAL_START + "Extremely_Obstructed/")

move_videos_to_testing(FROM_FILE_PATH_STARTER_UNCLASSIFIED, 
                        TO_FILE_PATH_TEST_START, 
                        number_of_extremely_obstructed_validation_videos)

# sort GOOD_TO_FAIR videos
number_of_good_to_fair_validation_videos = split_for_testing_and_validation(FROM_FILE_PATH_STARTER + "Good_to_Fair/", 
                                                                        TO_FILE_PATH_TRAIN_START + "Good_to_Fair/", 
                                                                        TO_FILE_PATH_VAL_START + "Good_to_Fair/")

move_videos_to_testing(FROM_FILE_PATH_STARTER_UNCLASSIFIED, 
                        TO_FILE_PATH_TEST_START, 
                        number_of_good_to_fair_validation_videos)

# sort POOR videos
number_of_poor_validation_videos = split_for_testing_and_validation(FROM_FILE_PATH_STARTER + "Poor/", 
                                                                        TO_FILE_PATH_TRAIN_START + "Poor/", 
                                                                        TO_FILE_PATH_VAL_START + "Poor/")

move_videos_to_testing(FROM_FILE_PATH_STARTER_UNCLASSIFIED, 
                        TO_FILE_PATH_TEST_START, 
                        number_of_poor_validation_videos)



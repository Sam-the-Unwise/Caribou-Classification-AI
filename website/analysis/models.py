from django.db import models
from multiselectfield import MultiSelectField




class Result(models.Model):
    File_Name = models.CharField(max_length=60, primary_key=True)
    Observer_Name = models.CharField(max_length=40)

    #--- excluded fields ---
    Cam_ID = models.IntegerField(default=0)
    Date = models.CharField(max_length=8, default='')
    Time = models.CharField(max_length=6, default='')
    Week_Num = models.IntegerField(default=0)
    #-----------------------

    Choices_Video_Quality = (
        ('Excellent', 'EXCELLENT'),
        ('Good_to_Fair', 'GOOD to FAIR'),
        ('Poor', 'POOR'),
        ('Extremely_Obstructed', 'EXTREMELY OBSTRUCTED'),
    )
    Video_Quality = models.CharField(max_length=20,
                                     choices=Choices_Video_Quality,)
#
    Choices_Ruminating_Foraging = (
        ('Chewing', 'CHEWING'),
        ('Drinking', 'DRINKING'),
        ('Eating', 'EATING'),
        ('Licking', 'LICKING soil for minerals but did not eat'),
        ('None', 'None of the above'),
        ('Ruminating', 'RUMINATING'),
    )
    Ruminating_Foraging=models.CharField(max_length=12,
                                         choices=Choices_Ruminating_Foraging,)

    Choices_State_of_Locomotion = (
        ('Napping', 'Napping'),
        ('Running', 'Running'),
        ('Stationary_Awake', 'Stationary Awake'),
        ('Wading/Swimming', 'Wading/Swimming'),
        ('Walking', 'Walking'),
    )
    State_of_Locomotion=models.CharField(max_length=20,
                                         choices=Choices_State_of_Locomotion,)

    Choices_Is_a_calf_visible = (
        ('No', 'No'),
        ('Yes_her_own', 'Yes – her own'),
        ('Yes_possibly_her_own', 'Yes – possibly her own'),
        ('Yes_with_another_cow', 'Yes – with another cow'),
    )
    Is_a_calf_visible=models.CharField(max_length=20,
                                       choices=Choices_Is_a_calf_visible,)

    Choices_Other_caribou_visible_excluding_own_calf = (
        ('No', 'No'),
        ('Yes', 'Yes'),
        ('Yes_herd', 'Yes – herd'),
        ('Yes_one_to_a_few', 'Yes – one to a few individuals'),
    )
    Other_caribou_visible_excluding_own_calf=models.CharField(max_length=20,
                                                              choices=Choices_Other_caribou_visible_excluding_own_calf,)

    Choices_Does_the_cow_have_antlers = (
        ('cant see', "Can't see/Not sure/Not relevant"),
        ('No', 'No'),
        ('Yes', 'Yes'),
    )
    Does_the_cow_have_antlers=models.CharField(max_length=20,
                                               choices=Choices_Does_the_cow_have_antlers,)

    MultiChoices_Potential_insect_avoidance_behavior = (
        ('Shook_its_head', 'Shook its head'),
        ('Kept_nose_Ground', 'Kept its nose still AND on the ground'),
        ('Scratched', 'Scratched'),
        ('Sought_snow_patch', 'Sought snow patch'),
        ('Huddled', 'Huddled'),
        ('None', 'None of the above'),
        #         # ('Kept_nose_Ground_Huddled', 'Kept its nose still AND on the ground, Huddled'),
        #         # ('Kept_nose_Ground_Huddled_Snow_patch', 'Kept its nose still AND on the ground, Sought snow patch'),
        #         # ('Potential_insect', 'Potential insect avoidance behavior'),
        #         # ('Shook_its_head_Huddled', 'Shook its head, Huddled'),
        #         # ('Shook_its_head_Kept_nose_Ground', 'Shook its head, Kept its nose still AND on the ground'),
        #         # ('Shook_its_head_Scratched', 'Shook its head, Scratched'),
        #         # ('Shook_its_head_Scratched_Huddled', 'Shook its head, Scratched, Huddled'),
    )
    Potential_insect_avoidance_behavior=MultiSelectField(choices=MultiChoices_Potential_insect_avoidance_behavior,
                                                         )

    Choices_What_part_of_the_habitat_is_visible = (
        ('Ground_immediate_surroundings', 'Ground and immediate surroundings'),
        ('None', 'None'),
        ('Only_ground', 'Only ground'),
    )
    What_part_of_the_habitat_is_visible=models.CharField(max_length=35,
                                                         choices=Choices_What_part_of_the_habitat_is_visible,)

    Choices_What_is_the_PREDOMINANT_vegetation = (
        ('Poor_visibility', 'Poor visibility of predominant vegetation'),
        ('Alpine_Tundra', 'Alpine Tundra'),
        ('Lichen/Moss/Herbaceous', 'Lichen/Moss/Herbaceous'),
        ('Shrubby', 'Shrubby'),
        ('Forested–Deciduous', 'Forested – Deciduous'),
        ('Forested–Coniferous', 'Forested – Coniferous'),
        ('Unvegetated_Areas', 'Unvegetated Areas'),
    )
    What_is_the_PREDOMINANT_vegetation=models.CharField(max_length=30,
                                                        choices=Choices_What_is_the_PREDOMINANT_vegetation,
                                                        )

    Choices_Habitat_features_visible = (
        ('Snow_cover_1–50%', 'Snow cover 1–50%'),
        ('Snow_cover_50–100%', 'Snow cover 50–100%'),
        ('Water', 'Water'),
        ('Burn_area', 'Burn area'),
        ('Human_signs', 'Human signs'),
        ('None', 'None of the above'),
    )
    Habitat_features_visible=models.CharField(max_length=20,
                                              choices=Choices_Habitat_features_visible,
                                              )

    # Other_species_detected = models.CharField(max_length=80)
    def __str__(self):
        return self.File_Name


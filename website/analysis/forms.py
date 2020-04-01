from analysis.models import Result
from django.forms import ModelForm
from django.contrib.auth.models import User


# create the form class.
class ResultForm(ModelForm):    # Inherit ModelForm class

    class Meta:
        model = Result          # target model
        fields = '__all__'      # 允许编辑的字段
        exclude = {'Cam_ID', 'Date', 'Time', 'Week_Num'}  # 排除的字段

    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields['Ruminating_Foraging'].required = False
        self.fields['State_of_Locomotion'].required = False
        self.fields['Is_a_calf_visible'].required = False
        self.fields['Other_caribou_visible_excluding_own_calf'].required = False
        self.fields['Does_the_cow_have_antlers'].required = False
        self.fields['Potential_insect_avoidance_behavior'].required = False
        self.fields['What_part_of_the_habitat_is_visible'].required = False
        self.fields['What_is_the_PREDOMINANT_vegetation'].required = False
        self.fields['Habitat_features_visible'].required = False

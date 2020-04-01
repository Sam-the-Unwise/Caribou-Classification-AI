from django.contrib import admin
from .models import Result

class ResultAdmin(admin.ModelAdmin):
    # search box
    # search_fields = ['Observer_Name']

    # Right column filter, filter by Observer_Name
    list_filter = ['Observer_Name']

    # Detailed time hierarchical filtering
    # date_hierarchy = 'created_time'

    list_display = ('File_Name',
                    'Observer_Name',
                    'Video_Quality',
                    'Ruminating_Foraging',
                    'State_of_Locomotion',
                    'Is_a_calf_visible',
                    'Other_caribou_visible_excluding_own_calf',
                    'Does_the_cow_have_antlers',
                    'Potential_insect_avoidance_behavior',
                    'What_part_of_the_habitat_is_visible',
                    'What_is_the_PREDOMINANT_vegetation',
                    'Habitat_features_visible',
                    )


# Register your models here.
admin.site.register(Result, ResultAdmin)



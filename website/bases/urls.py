from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bases-home'),
    path('training/', views.training, name='bases-training'),
    path('training/VideoQuality', views.training, name='training-video-quality'),
    path('training/Ruminating', views.training_ruminatingTutorial, name='training-ruminating'),
    path('training/Locomotion', views.training_locomotionTutorial, name='training-locomotion'),
    path('training/CalfVisible', views.training_calfVisibleTutorial, name='training-calf-visible'),
    path('training/otherCaribouVisible', views.training_otherCaribouVisibleTutorial,
         name='training-other-caribou-visible'),
    path('training/partHabitat', views.training_partHabitatTutorial,
         name='training-part-habitat'),
    path('training/vegetation', views.training_vegetationTutorial,
         name='training-vegetation'),
    path('training/habitatFeaturesVisible', views.training_habitatFeaturesVisibleTutorial,
         name='training-habitat-features-visible'),
    path('training/otherSpeciesDetected', views.training_otherSpeciesDetectedTutorial,
         name='training-other-species'),

    path('training-test/', views.training_test, name='bases-training-test'),

]

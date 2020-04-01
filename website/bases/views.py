from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'bases/home.html')

def training(request):
    return render(request, 'bases/videoTutorial.html')

def training_ruminatingTutorial(request):
    return render(request, 'bases/ruminatingTutorial.html')

def training_locomotionTutorial(request):
    return render(request, 'bases/locomotionTutorial.html')

def training_calfVisibleTutorial(request):
    return render(request, 'bases/calfVisibleTutorial.html')

def training_otherCaribouVisibleTutorial(request):
    return render(request, 'bases/otherCaribouVisibleTutorial.html')

def training_partHabitatTutorial(request):
    return render(request, 'bases/partHabitatTutorial.html')

def training_vegetationTutorial(request):
    return render(request, 'bases/vegetationTutorial.html')

def training_habitatFeaturesVisibleTutorial(request):
    return render(request, 'bases/habitatFeaturesVisibleTutorial.html')

def training_otherSpeciesDetectedTutorial(request):
    return render(request, 'bases/otherSpeciesDetectedTutorial.html')


def training_test(request):
    return render(request, 'bases/training_test.html')


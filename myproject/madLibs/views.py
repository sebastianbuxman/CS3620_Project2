from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import MadLib
from .forms import MadLibForm
import random

# Create your views here.
def index(response):
    return HttpResponse('hi there my name is sebastian')


def home(request):
    form = MadLibForm(request.POST or None)
    if form.is_valid():
        #form.save()
        adjective1 = form.cleaned_data['adjective1']
        place1 = form.cleaned_data['place1']
        verb1 = form.cleaned_data['verb1']
        noun1 = form.cleaned_data['noun1']
        adjective2 = form.cleaned_data['adjective2']
        verb2 = form.cleaned_data['verb2']
        noun2 = form.cleaned_data['noun2']
        random_number = random.randint(1, 15)
        madlib_story=""
        if random_number==1:
            madlib_story = f"The {adjective1} {place1} was {verb1} by a {noun1}. " \
                           f"The {adjective2} {noun2} {verb2} chased after it."
        elif random_number==2:
            madlib_story = f"The {place1} is a {adjective2} place even though we all think that {noun1} is " \
                           f"{adjective1}, we will {verb1} after {noun2} {verb2}."
        elif random_number==3:
            madlib_story = f"{noun1} loves {noun2} in {place1}, the cat {verb1} {adjective1} in {place1} even" \
                           f"though the dog {verb2} {adjective2}. "
        elif random_number==4:
            madlib_story = f"The {adjective2} {noun1} {verb1} over the {adjective1} {noun2} even though we all" \
                           f"{verb2} in {place1}"
        elif random_number==5:
            madlib_story = f"The {adjective1} {noun1} {verb2} at the {adjective2} {noun2}, while the couple {verb1} into" \
                           f"each others eyes in {place1}"
        elif random_number==6:
            madlib_story=f"The {noun1} was {verb1} by a {adjective1} {noun2}. It was a {adjective2} sight to behold while {noun2}" \
                         f"{verb2} laughing in {place1}"
        elif random_number==7:
            madlib_story = f"A {adjective1} {place1} was {verb1} by a {adjective2} {noun1}. The {noun2} " \
                           f"had to be captured and brought to justice {verb2}."
        elif random_number==8:
            madlib_story=f"While {verb1} in the {place1}, a {adjective1} {noun1} suddenly spotted a {adjective2} {noun2}" \
                         f" and decided to {verb2} it."
        elif random_number==9:
            madlib_story=f"The {place1} was known for its {adjective1} {noun1}s that would {verb1} and {verb2} around" \
                         f" the {adjective2} {noun2} statue."
        elif random_number ==10:
            madlib_story=f"The {adjective1} {noun1} was so {adjective2} that it decided to {verb1} all the way to the" \
                         f" {place1} and {verb2} there. While the {noun2} sat there laughing."
        elif random_number==11:
            madlib_story= f"The {adjective1} {noun1} was {verb1} by a {adjective2} {noun2}. The {noun1} {verb2} and the" \
                          f" {noun2} {verb1} in response. They were situated in {place1}"
        elif random_number==12:
            madlib_story = f"As the {noun1} {verb1} through the {place1}, a {adjective1} {noun2} emerged from the" \
                           f" shadows. The {noun2} tried to {verb2}, but was no match for the {noun1}'s {adjective2} {verb1}."
        elif random_number==13:
            madlib_story= f"The {adjective1} {noun1} {verb1} across the {place1}, leaving a trail of {adjective2} {noun2} " \
                          f"in its wake. The {noun2} {verb2} to catch up, but could not keep pace with the {noun1}'s {adjective1} speed."
        elif random_number==14:
            madlib_story=f"The {adjective1} {noun1} ran into the {adjective2} {place1} and {verb1} the {noun2}, {verb2}."
        elif random_number==15:
            madlib_story=f"While {verb1} through the {place1}, the {adjective1} {noun1} saw the {adjective2} {noun2} " \
                         f"and stopped to say hello. While the {noun2} {verb2}"


        # Create and save new MadLib object with the story
        new_madlib = MadLib(adjective1=adjective1, place1=place1, verb1=verb1, noun1=noun1,
                            adjective2=adjective2, verb2=verb2, noun2=noun2, story=madlib_story)
        new_madlib.save()
        return redirect('madlibs:madlibs_result')
    return render(request, 'madLibs/base.html', {'form': form})

def madlibs_result(request):
    latest_madlib = MadLib.objects.latest('id')
    return render(request, 'madLibs/story.html', {'story': latest_madlib.story})


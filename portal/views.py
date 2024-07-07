# alumni/views.py
from django.shortcuts import render, redirect
from .forms import AlumniForm, QuestionnaireForm
from .models import Alumni, Questionnaire
from django.contrib import messages

def alumni_create_view(request):
    if request.method == 'POST':
        alumni_form = AlumniForm(request.POST, request.FILES)
        questionnaire_form = QuestionnaireForm(request.POST)
        if alumni_form.is_valid() and questionnaire_form.is_valid():
            alumni = alumni_form.save()
            alumni.save()
            questionnaire = questionnaire_form.save(commit=False)
            questionnaire.alumni = alumni
            questionnaire.save()
            messages.success(request, 'Profile added successfully.')
            return redirect('alumni_create')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        alumni_form = AlumniForm()
        questionnaire_form = QuestionnaireForm()
    return render(request, 'portal/alumni_form.html', {'alumni_form': alumni_form, 'questionnaire_form': questionnaire_form})


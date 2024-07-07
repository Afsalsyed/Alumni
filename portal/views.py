# alumni/views.py
from django.shortcuts import render, redirect
from .forms import AlumniForm, QuestionnaireForm
from .models import Alumni, Questionnaire

def alumni_create_view(request):
    if request.method == 'POST':
        alumni_form = AlumniForm(request.POST, request.FILES)
        #print(alumni_form)
        questionnaire_form = QuestionnaireForm(request.POST)
        #print(questionnaire_form)
        if alumni_form.is_valid() and questionnaire_form.is_valid():
            alumni = alumni_form.save()
            alumni.save()
            questionnaire = questionnaire_form.save(commit=False)
            questionnaire.alumni = alumni
            questionnaire.save()
            return redirect('alumni_success')
    else:
        alumni_form = AlumniForm()
        questionnaire_form = QuestionnaireForm()
    return render(request, 'portal/alumni_form.html', {'alumni_form': alumni_form, 'questionnaire_form': questionnaire_form})

def alumni_success_view(request):
    return render(request, 'portal/alumni_success.html')

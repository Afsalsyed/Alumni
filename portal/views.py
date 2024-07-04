from django.shortcuts import render, redirect # type: ignore
from django.http import JsonResponse # type: ignore
from .models import Alumni, Questionnaire, YearOfStudy
from .forms import AlumniForm, QuestionnaireForm # type: ignore

def alumni_form_view(request):
    if request.method == 'POST':
        alumni_form = AlumniForm(request.POST, request.FILES, prefix='alumni')
        questionnaire_form = QuestionnaireForm(request.POST, prefix='questionnaire')

        if alumni_form.is_valid() and questionnaire_form.is_valid():
            alumni = alumni_form.save()
            questionnaire = questionnaire_form.save(commit=False)
            questionnaire.alumni = alumni
            questionnaire.save()
            return JsonResponse({'success': True})
        else:
            errors = {
                'alumni_errors': alumni_form.errors,
                'questionnaire_errors': questionnaire_form.errors
            }
            return JsonResponse({'success': False, 'errors': errors})

    else:
        alumni_form = AlumniForm(prefix='alumni')
        questionnaire_form = QuestionnaireForm(prefix='questionnaire')

    context = {
        'alumni_form': alumni_form,
        'questionnaire_form': questionnaire_form
    }
    return render(request, 'portal/alumni_form.html', context)

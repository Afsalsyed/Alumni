from django.shortcuts import render, redirect # type: ignore
from django.http import JsonResponse # type: ignore
from .models import Alumni, Questionnaire, YearOfStudy
from .forms import AlumniForm, QuestionnaireForm # type: ignore
from django.db import transaction # type: ignore

def alumni_form_view(request):
    if request.method == 'POST':
        alumni_form = AlumniForm(request.POST, request.FILES, prefix='alumni')
        questionnaire_form = QuestionnaireForm(request.POST, prefix='questionnaire')

        try:
            with transaction.atomic():
                if alumni_form.is_valid() and questionnaire_form.is_valid():
                    alumni = alumni_form.save(commit=False)
                    if alumni_form.cleaned_data['educational_qualification'] == 'O':
                        alumni.educational_qualification = alumni_form.cleaned_data['educational_qualification_other']
                    alumni.save()

                    questionnaire = questionnaire_form.save(commit=False)
                    questionnaire.alumni = alumni
                    questionnaire.save()

                    print("Alumni data saved successfully:", alumni)
                    print("Questionnaire data saved successfully:", questionnaire)

                    return JsonResponse({'success': True})
                else:
                    errors = {
                        'alumni_errors': alumni_form.errors,
                        'questionnaire_errors': questionnaire_form.errors
                    }
                    print("Form errors:", errors)
                    return JsonResponse({'success': False, 'errors': errors})

        except Exception as e:
            print("Error saving data:", str(e))
            return JsonResponse({'success': False, 'errors': str(e)})

    else:
        alumni_form = AlumniForm(prefix='alumni')
        questionnaire_form = QuestionnaireForm(prefix='questionnaire')

    context = {
        'alumni_form': alumni_form,
        'questionnaire_form': questionnaire_form
    }
    return render(request, 'portal/alumni_form.html', context)
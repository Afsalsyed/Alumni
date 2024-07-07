# alumni/forms.py
from django import forms
from .models import Alumni, Questionnaire, Year

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'educational_qualification': forms.RadioSelect(),
            'course_of_study': forms.RadioSelect(),
            'employment_status': forms.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super(AlumniForm, self).__init__(*args, **kwargs)
        # self.fields['gender'].initial = 'M'
        # self.fields['educational_qualification'].initial = 'B.Pharm'
        #self.fields['employment_status'].initial = 'Emp'
        self.fields['ug_year_of_study'].queryset = Year.objects.filter(degree='UG')
        self.fields['pg_year_of_study'].queryset = Year.objects.filter(degree__startswith='PG')
        self.fields['other_qualification'].widget.attrs.update({'id': 'id_other_qualification'})
        self.fields['other_qualification'].required = False

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = [
            'alumni_meet', 'guest_college_event', 'resource_person', 'mentor_research_papers',
            'college_event_management', 'college_outreach_program', 'college_promotional_endeavor',
            'job_refer', 'placement_cell'
        ]
        widgets = {
            field: forms.RadioSelect()
            for field in fields
        }
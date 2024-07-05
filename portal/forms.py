from django import forms # type: ignore
from .models import Alumni, Questionnaire, YearOfStudy

class AlumniForm(forms.ModelForm):
    educational_qualification_other = forms.CharField(required=False, label="Other Educational Qualification", widget=forms.TextInput(attrs={'style': 'display:none;'}))
    gender = forms.ChoiceField(choices=Alumni.GENDER_CHOICES, widget=forms.RadioSelect)
    educational_qualification = forms.ChoiceField(choices=Alumni.EDUCATIONAL_QUALIFICATION_CHOICES, widget=forms.RadioSelect)
    course_of_study = forms.ChoiceField(choices=Alumni.COURSE_OF_STUDY_CHOICES, widget=forms.RadioSelect)
    employment_status = forms.ChoiceField(choices=Alumni.EMPLOYMENT_STATUS_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Alumni
        fields = [
            'email', 'name', 'gender', 'date_of_birth', 'contact_number',
            'present_address', 'permanent_address', 'educational_qualification',
            'course_of_study', 'ug_year_of_study', 'pg_year_of_study',
            'photo', 'employment_status', 'company_name', 'current_designation',
            'company_location', 'company_address', 'higher_study_details'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].initial = 'M'
        self.fields['educational_qualification'].initial = 'B.Pharm'
        self.fields['course_of_study'].initial = 'UG'
        self.fields['ug_year_of_study'].queryset = YearOfStudy.objects.filter(degree='UG')
        self.fields['pg_year_of_study'].queryset = YearOfStudy.objects.filter(degree__startswith='PG')

        if self.data.get('educational_qualification') == 'O':
            self.fields['educational_qualification_other'].widget.attrs['style'] = 'display:block;'

    def clean(self):
        cleaned_data = super().clean()
        educational_qualification = cleaned_data.get('educational_qualification')
        educational_qualification_other = cleaned_data.get('educational_qualification_other')
        
        if educational_qualification == 'O' and not educational_qualification_other:
            self.add_error('educational_qualification_other', 'This field is required.')

        return cleaned_data


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
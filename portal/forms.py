from django import forms # type: ignore
from .models import Alumni, Questionnaire

class AlumniForm(forms.ModelForm):
    educational_qualification_other = forms.CharField(required=False, label="Other Educational Qualification")

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
            'gender': forms.RadioSelect(),
            'educational_qualification': forms.RadioSelect(),
            'course_of_study': forms.RadioSelect(),
            'employment_status': forms.RadioSelect(),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = [
            'alumni_meet', 'guest_college_event', 'resource_person', 'mentor_research_papers',
            'college_event_management', 'college_outreach_program', 'college_promotional_endeavor',
            'job_refer', 'placement_cell'
        ]
        widgets = {
            'alumni_meet': forms.RadioSelect(),
            'guest_college_event': forms.RadioSelect(),
            'resource_person': forms.RadioSelect(),
            'mentor_research_papers': forms.RadioSelect(),
            'college_event_management': forms.RadioSelect(),
            'college_outreach_program': forms.RadioSelect(),
            'college_promotional_endeavor': forms.RadioSelect(),
            'job_refer': forms.RadioSelect(),
            'placement_cell': forms.RadioSelect()
        }

# alumni/admin.py
from django.contrib import admin
from .models import Alumni, Questionnaire

class AlumniAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'gender', 'date_of_birth', 'contact_number')
        }),
        ('Address', {
            'fields': ('present_address', 'permanent_address')
        }),
        ('Education', {
            'fields': ('educational_qualification', 'other_qualification', 'course_of_study', 'ug_year_of_study', 'pg_year_of_study')
        }),
        ('Employment', {
            'fields': ('employment_status', 'company_name', 'current_designation', 'company_location', 'company_address', 'higher_study_details')
        }),
        ('Photo', {
            'fields': ('photo',)
        }),
    )

    list_display = (
        'name', 'email', 'gender', 'date_of_birth', 'contact_number', 
        'present_address', 'permanent_address', 'educational_qualification', 
        'course_of_study', 'ug_year_of_study', 'pg_year_of_study', 'photo', 
        'employment_status', 'company_name', 'current_designation', 
        'company_location', 'company_address', 'higher_study_details'
    )
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('gender', 'educational_qualification', 'course_of_study', 'employment_status')

class QuestionnaireAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Alumni', {
            'fields': ('alumni',)
        }),
        ('Participation', {
            'fields': ('alumni_meet', 'guest_college_event', 'resource_person', 'mentor_research_papers', 'college_event_management', 'college_outreach_program', 'college_promotional_endeavor', 'job_refer', 'placement_cell')
        }),
    )

    list_display = (
        'alumni', 'alumni_meet', 'guest_college_event', 'resource_person', 
        'mentor_research_papers', 'college_event_management', 
        'college_outreach_program', 'college_promotional_endeavor', 
        'job_refer', 'placement_cell'
    )
    search_fields = ('alumni__name', 'alumni__email')
    list_filter = ('alumni_meet', 'guest_college_event', 'resource_person')

admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)

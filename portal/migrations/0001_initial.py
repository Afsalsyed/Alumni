# Generated by Django 5.0.6 on 2024-07-07 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1)),
                ('date_of_birth', models.DateField()),
                ('contact_number', models.CharField(max_length=10, unique=True)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('educational_qualification', models.CharField(choices=[('B.Pharm', 'B.Pharm'), ('M.Pharm', 'M.Pharm'), ('PhD', 'PhD'), ('O', 'Other')], default='B.Pharm', max_length=10)),
                ('other_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('course_of_study', models.CharField(choices=[('UG', 'UG'), ('PG-Pharmaceutics)', 'PG (M.Pharm - Pharmaceutics)'), ('PG-Pharmacology)', 'PG (M.Pharm - Pharmacology)')], default='UG', max_length=20)),
                ('photo', models.ImageField(upload_to='profile/')),
                ('employment_status', models.CharField(blank=True, choices=[('Emp', 'Employee'), ('Entrepreneur', 'Entrepreneur'), ('Unemp', 'Unemployed'), ('Home maker', 'Home maker / House wife')], default='Emp', max_length=12, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('current_designation', models.CharField(blank=True, max_length=255, null=True)),
                ('company_location', models.CharField(blank=True, max_length=255, null=True)),
                ('company_address', models.TextField(blank=True, null=True)),
                ('higher_study_details', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')], max_length=2)),
                ('start_year', models.PositiveIntegerField()),
                ('end_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumni_meet', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Would you like to come for Alumni Meet, if the Institute organizes the same')),
                ('guest_college_event', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Do you have a wish to present yourself as a guest of our college events')),
                ('resource_person', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Willing to accept our invitation to you to act as a resource person')),
                ('mentor_research_papers', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Willful to be a mentor for any research projects to our students')),
                ('college_event_management', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Do you like to get involved in our college events management')),
                ('college_outreach_program', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Will you be intentional to participate in any of our college social out-reach programs')),
                ('college_promotional_endeavor', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Do you have an unforced desirous to contribute your valuable experience and timings for any of the college promotion endeavors')),
                ('job_refer', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Are you willing to refer any jobs to your college junior')),
                ('placement_cell', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Do you like to contribute to KCP placement cell')),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.alumni')),
            ],
        ),
        migrations.AddField(
            model_name='alumni',
            name='pg_year_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pg_year', to='portal.year'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='ug_year_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ug_year', to='portal.year'),
        ),
    ]

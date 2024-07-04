from django.db import models # type: ignore


class YearOfStudy(models.Model):
    DEGREE_CHOICES=[
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    degree = models.CharField(max_length=2, choices=DEGREE_CHOICES)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.degree} - {self.start_year} - {self.end_year}  "


class Alumni(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ]

    EDUCATIONAL_QUALIFICATION_CHOICES = [
        ('B.Pharm', 'B.Pharm'),
        ('M.Pharm', 'M.Pharm'),
        ('PhD', 'PhD'),
        ('O', 'Others')
    ]


    COURSE_OF_STUDY_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG-Pharmaceutics)', 'PG (M.Pharm - Pharmaceutics)'),
        ('PG-Pharmacology)', 'PG (M.Pharm - Pharmacology)')
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('Emp', 'Employee'),
        ('Entrepreneur', 'Entrepreneur'),
        ('Unemp', 'Unemployed'),
        ('Homemaker', 'Home maker / House wife')
    ]

 
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=10, unique=True)
    present_address = models.TextField()
    permanent_address = models.TextField()
    educational_qualification = models.CharField(max_length=10, choices=EDUCATIONAL_QUALIFICATION_CHOICES)
    course_of_study = models.CharField(max_length=20, choices=COURSE_OF_STUDY_CHOICES)
    ug_year_of_study = models.ForeignKey(YearOfStudy, related_name='ug_year', on_delete=models.CASCADE, null=True, blank=True)
    pg_year_of_study = models.ForeignKey(YearOfStudy, related_name='pg_year', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='profile/')
    employment_status = models.CharField(max_length=12, choices=EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    current_designation = models.CharField(max_length=255, null=True, blank=True)
    company_location = models.CharField(max_length=255, null=True, blank=True)
    company_address = models.TextField(null=True, blank=True)
    higher_study_details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):  
        return self.name

class Questionnaire(models.Model):
    Q_CHOICES= [
        ('True', 'Yes'),
        ('False', 'No'),
        
    ]

    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    alumni_meet = models.BooleanField(verbose_name = "Would you like to come for Alumni Meet, if the Institute organizes the same", choices=Q_CHOICES, default=False)
    guest_college_event = models.BooleanField(verbose_name = "Do you have a wish to present yourself as a guest of our college events",choices=Q_CHOICES, default=False)
    resource_person = models.BooleanField(verbose_name = "Willing to accept our invitation to you to act as a resource person", choices=Q_CHOICES, default=False)
    mentor_research_papers = models.BooleanField(verbose_name = "Willful to be a mentor for any research projects to our students", choices=Q_CHOICES, default=False)
    college_event_management =models.BooleanField(verbose_name = "Do you like to get involved in our college events management", choices=Q_CHOICES, default=False)
    college_outreach_program = models.BooleanField(verbose_name = "Will you be intentional to participate in any of our college social out-reach programs", choices=Q_CHOICES, default=False)
    college_promotional_endeavor = models.BooleanField(verbose_name = "Do you have an unforced desirous to contribute your valuable experience and timings for any of the college promotion endeavors", choices=Q_CHOICES, default=False)
    job_refer = models.BooleanField(verbose_name = "Are you willing to refer any jobs to your college junior", choices=Q_CHOICES, default=False)
    placement_cell= models.BooleanField(verbose_name = "Do you like to contribute to KCP placement cell", choices=Q_CHOICES, default=False)

    def __str__(self):
        return self.alumni.name



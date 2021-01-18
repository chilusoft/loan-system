from django.db import models

# Create your models here.
class ProgramOfStudy(models.Model):
    Y1 = 'Bachelor of Information and Comm..'
    Y2 = 'Bachelor of Mathematics'
    Y3 = 'Bachelor of Economics'
    Y4 = 'Bachelor of Laws'

    programs = [
        (Y1, 'BICT'),
        (Y2, 'BEd Math'),
        (Y3, 'BSc.EC'),
        (Y4, 'BSc. LLB')
    ]
    program_name = models.CharField(max_length=255, choices=programs, default=Y1)

    def __str__(self):

        return self.program_name

class StudentProfile(models.Model):

    Y1 = 'Freshman'
    Y2 = 'Sophomore'
    Y3 = 'Senior'
    Y4 = 'Graduate'

    STUDY_YEAR = [
        (Y1, '1st'),
        (Y2, '2nd'),
        (Y3, '3rd'),
        (Y4, '4th')
    ]
    program = models.ForeignKey(ProgramOfStudy, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.IntegerField()
    year_of_study = models.CharField(max_length=14, choices=STUDY_YEAR, default=Y1)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return str(self.student_id) + ' | ' +self.last_name + ' ' +self.first_name + ' | ' + str(self.program)


class Courses(models.Model):

    student = models.ForeignKey(ProgramOfStudy, on_delete=models.CASCADE)
    sbj1 = models.CharField(max_length=255)
    sbj2 = models.CharField(max_length=255)
    sbj3 = models.CharField(max_length=255)
    sbj4 = models.CharField(max_length=255)

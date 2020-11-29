from django.db import models


class Vacancy(models.Model):
    profession = models.CharField(max_length=100)

    schedule = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

    experience = models.PositiveIntegerField(default=0)
    skills = models.CharField(max_length=100)
    achievements = models.CharField(max_length=300, blank=True)
    expectations = models.CharField(max_length=100)
    add_info = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Резюме'


# {
#         "profession": "Senior Python Developer",
#         "schedule": 40,
#         "employment": "flex",
#         "education": "master",
#         "salary": 200000,
#         "experience": 5,
#         "skills": "Python, matplotlib, pandas",
#         "achievements": "text",
#         "expectations": "text",
#         "add_info": "text",
#         "feedback": "text"
# }
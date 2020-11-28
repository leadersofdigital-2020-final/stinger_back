from django.db import models


class CV(models.Model):
    profession = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
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

    # def __str__(self):
    #     return self.title
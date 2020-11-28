from django.db import models


class CV(models.Model):
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    
    image = models.CharField(max_length=300)
    video = models.CharField(max_length=100)

    stage = models.PositiveIntegerField(default=0)
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
    phone = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Резюме'

    # def __str__(self):
    #     return self.title
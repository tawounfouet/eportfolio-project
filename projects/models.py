from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Project(models.Model):
    class Field(models.TextChoices):
        MACHINE_LEARNING = 'ML'
        DEEP_LEARNING = 'DL'
        DATA_SCIENCE = 'DS'
        DATA_ANALYSIS = "DA"
        DATA_ENGINEERING = "DE"

    name = models.fields.CharField(max_length=100)
    
    #goals = models.fields.CharField(max_length=2000)
    
    field = models.fields.CharField(max_length=5, choices=Field.choices)
    year_created = models.fields.IntegerField(validators=[MinValueValidator(2000), 
                                                        MaxValueValidator(2025)])
    #description = models.fields.CharField(max_length=10000)
    active = models.fields.BooleanField(default=True)
    summary = models.fields.TextField(blank=True, verbose_name="Résumé du projet")
    skills = models.fields.TextField(blank=True, verbose_name="Compétences cibles")
    description = models.TextField(blank=True, verbose_name="Description du projet")
    thumbnail = models.ImageField(blank=True, upload_to='photos/project')

    
    

    def __str__(self):
        return f'{self.name}'
from django.db import models
from django.contrib.auth.models import User

Language_CHOICES=[
    ('EN', 'English'),
    ('NP', 'Nepali'),
    ('JP', 'Japanese'),
    ('HI', 'HINDI'),
]


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)
    page_count=models.IntegerField()
    language=models.CharField(max_length=50,choices=Language_CHOICES, default="EN")
    def __str__(self):
        return self.title
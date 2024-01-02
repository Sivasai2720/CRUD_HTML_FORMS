from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=70,primary_key=True)
    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    matches_win=models.CharField(max_length=20)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name

    

from django.db import models

# Create your models here.
class Grade (models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class Subject (models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Lesson (models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()


    def __str__(self):
        return self.title
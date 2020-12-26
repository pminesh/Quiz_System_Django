from django.db import models

# Create your models here.

class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=15)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class QuizCourse(models.Model):
    coursename = models.CharField(max_length=100)

    def __str__(self):
        return self.coursename
            
class Quiz_Quistion(models.Model):
    quiz_type = models.ForeignKey(QuizCourse, on_delete=models.CASCADE)
    qustion = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.qustion
    
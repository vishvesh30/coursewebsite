from django.db import models
from joinus.models import student, instructor


# Create your models here.

class course(models.Model):
    cname=models.CharField(max_length=50)
    creatorid=models.ForeignKey(instructor,on_delete=models.CASCADE)
    taughtby=models.CharField(max_length=50)
    prerequisite=models.CharField(max_length=200)
    course_language=models.CharField(max_length=30)
    duration=models.IntegerField()
    fee=models.IntegerField(default=0)
    start_date=models.CharField(max_length=12)
    course_pic=models.FileField(default='abc.jpg')

    def __str__(self):
        return self.cname

class enrolldata(models.Model):
    student_id=models.ForeignKey(student)
    course_id=models.ForeignKey(course)
    join_date=models.DateField(default='2017-12-31')
    def __str__(self):
        return self.course_id.cname+'-'+self.student_id.uname

class coursecontent(models.Model):
    course_id = models.ForeignKey(course,on_delete=models.CASCADE)
    content_sub_id = models.IntegerField(default=0)
    content_name = models.CharField(max_length=50)
    content_description = models.CharField(max_length=500,default='description')
    content_type = models.CharField(default='null',max_length=10)
    content_url = models.FileField(default='abc.mp4')
    content_sequence_no = models.IntegerField(default=-1)
    def __str__(self):
        return self.content_name +'-'

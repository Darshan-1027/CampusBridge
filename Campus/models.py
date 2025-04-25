from django.db import models
from django.utils.html import mark_safe

# Create your models here.

Gender = [('M',"Male"),
          ('F',"Female")]

class CollegesModel(models.Model):

    Clg_name = models.CharField(max_length=50)
    Countryname = models.CharField(max_length=30,default="India")
    Statename = models.CharField(max_length=30,default="Gujarat")
    Cityname = models.CharField(max_length=30,default="Ahmedabad")
    ContactNo = models.BigIntegerField()
    EmailId = models.EmailField()
    AdministrationName = models.CharField(max_length=50)
    Administration_No = models.BigIntegerField()
    Password = models.CharField(max_length=15,default="dp1234")
    Approval = models.BooleanField(default=False)
    Time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Clg_name
    
class FacultyModel(models.Model):

    Faculty_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    BirthDate = models.DateField()
    Faculty_phone_no = models.BigIntegerField()
    FacultyEmail = models.EmailField()
    FacultyAddress = models.TextField(max_length=250)
    CollegeName = models.ForeignKey(CollegesModel,on_delete=models.CASCADE)
    EntrolmentNo = models.CharField(max_length=20)
    DepartMent = models.CharField(max_length=30)
    Document = models.ImageField(upload_to="media/Faculty_documents")
    Password = models.CharField(max_length=15,default="dp1234")
    Approval = models.BooleanField(default=False)
    Time = models.DateField(auto_now=True)

    def document_url(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Document.url))
 


class StudentModel(models.Model):

    Student_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=20)
    BirthDate = models.DateField()
    Student_No = models.BigIntegerField()
    Student_Emailid = models.EmailField()
    Address = models.TextField()
    Student_EntrollNo = models.CharField(max_length=20)
    StudentCourse = models.CharField(max_length=30)
    StudentSemester = models.CharField(max_length=30)
    College = models.ForeignKey(CollegesModel,on_delete=models.CASCADE)
    Password = models.CharField(max_length=15,default="dp1234")
    Approval = models.BooleanField(default=False)
    Time = models.DateTimeField(auto_now=True)



    


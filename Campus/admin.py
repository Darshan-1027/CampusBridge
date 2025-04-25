from django.contrib import admin
from .models import *

# Register your models here.

class Colleges(admin.ModelAdmin):

    list_display = ["Clg_name","Countryname","Statename","Cityname","ContactNo","EmailId","AdministrationName","Administration_No","Password","Approval","Time"]

admin.site.register(CollegesModel,Colleges)

class Facultys(admin.ModelAdmin):

    list_display = ["Faculty_name","Gender","BirthDate","Faculty_phone_no","FacultyEmail","FacultyAddress","CollegeName","EntrolmentNo","DepartMent","document_url","Password","Approval","Time"]

admin.site.register(FacultyModel,Facultys)


class Students(admin.ModelAdmin):

    list_display=["Student_name","Gender","BirthDate","Student_No","Student_Emailid","Address","Student_EntrollNo","StudentCourse","StudentSemester","College","Password","Approval","Time"]

admin.site.register(StudentModel,Students)

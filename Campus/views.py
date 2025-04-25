from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

Collegelogin = False
FacultyLogin = False
StudentLogin = False

def HomePage(request):
    return render(request,"CampusBridge.html")

def CollegeCampusPage(request):
    return render(request,"CollegeCumpus.html")

def FacultyCampusPage(request):
    return render(request,"FacultyCampus.html")

def StudentCampusPage(request):
    return render(request,"StudentCampus.html")


def LoginPage(request):
    return render(request,"LoginClass.html")

def LoginCheck(request):

    if request.method=="POST":
        email = request.POST.get("emailid")
        password = request.POST.get("password")

        print(email,"\n",password)

        CollegeData = CollegesModel.objects.filter(EmailId=email,Password=password).first()
        FacultyData = FacultyModel.objects.filter(FacultyEmail=email,Password=password).first()
        StudentData = StudentModel.objects.filter(Student_Emailid=email,Password=password).first()

        if CollegeData:

            if CollegeData.Approval==True:


                request.session["clg_name"] = CollegeData.Clg_name
                request.session["clg_no"] = CollegeData.ContactNo
                request.session["clg_email"] = CollegeData.EmailId

                Collegelogin = True
                print(Collegelogin)

                return redirect("/collegehomepage")
            else:
                messages.success(request,"Your college registration is pending approval. Once approved by the admin, you can access the portal.")

        elif FacultyData:

            if FacultyData.Approval==True:


                request.session["faculty_name"] = FacultyData.Faculty_name
                request.session["faculty_no"] = FacultyData.Faculty_phone_no
                request.session["faculty_email"] = FacultyData.FacultyEmail

                FacultyLogin = True
                print(FacultyLogin)

                return redirect("/facultyhomepage")
            else:
                messages.success(request,"Your profile is under review by your college admin. You will be able to log in after approval.")

        elif StudentData:

            if StudentData.Approval==True:


                request.session["student_name"] = StudentData.Student_name
                request.session["student_no"] = StudentData.Student_No
                request.session["student_email"] = StudentData.Student_Emailid

                StudentLogin = True
                print(StudentLogin)

                return redirect("/studenthomepage")
            else:
                messages.success(request,"Your student account is waiting for college approval. Please check back once your registration is approved.")
        else:
            messages.error(request,"Invalid Email Or Password")


    return redirect("/loginpage")

def Logout(request):

    if Collegelogin==True:

        del request.session["clg_name"]
        del request.session["clg_no"]
        del request.session["clg_email"]


    elif FacultyLogin==True:

        del request.session["faculty_name"]
        del request.session["faculty_no"] 
        del request.session["faculty_email"]
 
        
    elif StudentLogin==True:
        
        del request.session["student_name"] 
        del request.session["student_no"] 
        del request.session["student_email"]

    else:
        pass


    return redirect("/")


def RegistrationPage(request):

    collegedata = CollegesModel.objects.all().order_by('-id')

    contex = {

        "colleges" : collegedata
    }

    return render(request,"RegistrationPage.html",contex)

def CollegeRegistrationDataStore(request):

    if request.method=="POST":

        collegename = request.POST.get("college_name")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")
        contactno = request.POST.get("phone_no")
        emailid = request.POST.get("emailid")
        administartionname = request.POST.get("admin_name")
        admin_contact_no = request.POST.get("admin_contact_no")
        password = request.POST.get("password")

        print(collegename,country,state,city,contactno,emailid,administartionname,admin_contact_no,password)

        CheckEmail = CollegesModel.objects.filter(EmailId=emailid)

        if CheckEmail:
            messages.error(request,"This Email Id Already Exiest")
            return redirect("/registrationpage")
        else:

            Quiry = CollegesModel(Clg_name=collegename,Countryname=country,Statename=state,Cityname=city,ContactNo=contactno,EmailId=emailid,AdministrationName=administartionname,Administration_No=admin_contact_no,Password=password)
            Quiry.save()

            messages.success(request,"Thank you for registering your college with CampusBridge! Your application is under review by our team. We will notify you once your college is approved")

    return redirect("/loginpage")
    
    
def FacultyRegistrationDataStore(request):

    if request.method=="POST":

        facultyname = request.POST.get("faculty_name")
        gender = request.POST.get("gender")
        birthdate = request.POST.get("date")
        faculty_no = request.POST.get("faculty_number")
        faculty_email = request.POST.get("faculty_emailid")
        faculty_address = request.POST.get("address")
        college = request.POST.get("colleges")
        entrollment_no = request.POST.get("faculty_entroll_no")
        department = request.POST.get("departments")
        documents = request.FILES["document"]
        password = request.POST.get("password")

        print(facultyname,gender,birthdate,faculty_no,faculty_email,faculty_address,college,entrollment_no,department,documents,password)

        CheckEmail = FacultyModel.objects.filter(FacultyEmail=faculty_email)

        if CheckEmail:
            messages.error(request,"This Email Id Already Exiest")
            return redirect("/registrationpage")
        else:

            Quiry = FacultyModel(Faculty_name=facultyname,Gender=gender,BirthDate=birthdate,Faculty_phone_no=faculty_no,FacultyEmail=faculty_email,FacultyAddress=faculty_address,
                                CollegeName=CollegesModel(id=college),EntrolmentNo=entrollment_no,DepartMent=department,
                                Document=documents,Password=password)
            Quiry.save()
        
            messages.success(request, "Thank you for registering! Your profile is submitted and pending approval. You will be notified once approved.")


    return redirect("/loginpage")

def StudendRegistrationDataStore(request):

    if request.method=="POST":
        
        studentname = request.POST.get("student_name")
        gender = request.POST.get("gender")
        birthdate = request.POST.get("date")
        student_no = request.POST.get("call_no")
        student_email = request.POST.get("email")
        student_address = request.POST.get("address")
        student_entrollment_no = request.POST.get("numberentrollment")
        student_course = request.POST.get("courses")
        student_semester = request.POST.get("semester")
        college = request.POST.get("colleges")
        password = request.POST.get("password")
        

        print(studentname,gender,birthdate,student_no,student_email,student_address,student_entrollment_no,student_course,student_semester,college,password)

        CheckEmail = StudentModel.objects.filter(Student_Emailid=student_email)

        if CheckEmail:
            messages.error(request,"This Email Id Already Exiest")
            return redirect("/registrationpage")
        else:

            Quiry = StudentModel(Student_name=studentname,Gender=gender,BirthDate=birthdate,Student_No=student_no,Student_Emailid=student_email,Address=student_address,Student_EntrollNo=student_entrollment_no,StudentCourse=student_course,StudentSemester=student_semester,College=CollegesModel(id=college),Password=password)
            Quiry.save()
            messages.success(request, "Thank you for registering! Your profile is submitted and awaiting approval by your college Faculty. Once approved, you will be able to log in.")
            

    return redirect("/loginpage")













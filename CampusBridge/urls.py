"""
URL configuration for CampusBridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Campus import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage),
    path('loginpage',views.LoginPage),
    path('logincheck',views.LoginCheck),
    path('logout',views.Logout),
    path('collegehomepage',views.CollegeCampusPage),
    path('facultyhomepage',views.FacultyCampusPage),
    path('studenthomepage',views.StudentCampusPage),
    path('registrationpage',views.RegistrationPage),
    path('collegedatastore',views.CollegeRegistrationDataStore),
    path('facultydatastore',views.FacultyRegistrationDataStore),
    path('studentdatastore',views.StudendRegistrationDataStore),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

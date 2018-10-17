"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

import apps.course.urls as course_routes
import apps.student.urls as student_routes
import apps.grade.urls as grade_routes
import apps.auth.urls as auth_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(auth_routes)),
    path('course/', include(course_routes)),
    path('student/', include(student_routes)),
    path('grade/', include(grade_routes)),
    path('', login_required(TemplateView.as_view(template_name='modules/index/index.html')), name='homepage'),
]

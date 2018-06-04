from django.conf.urls import url,include
from api.views import course,login

from rest_framework import routers
routers=routers.DefaultRouter()
routers.register(r'course',course.CourseModelViews)
routers.register(r'degreecourse',course.DegreeCourselModelViews)
routers.register(r'teacher',course.TeacherModelViews)
routers.register(r'course/detail',course.CourseDetailModelViews)
routers.register(r'news',course.MicroView)
routers.register(r'news/detail',course.NewDetailView)

urlpatterns = [
    url(r'^',include(routers.urls)),
    url(r'auth/$',login.Authview.as_view()),
]
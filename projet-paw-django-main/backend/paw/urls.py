from django.urls import path
from . import views
from .views import  TasksView, IndexView, AboutView, AccountView, MotivationView, CalendarView , auth_view, user_logout, TasksStat

#from users import user_views

urlpatterns = [
    path('tasks/', TasksView.as_view(), name="task"), 
    path("account/",TasksStat.as_view(), name="account"),
    path("motivation/",MotivationView.as_view(), name="motivation"),
    path("calendar/",CalendarView.as_view(), name="calendar"),
    path('', auth_view,name="auth_view"),
    path('about/', AboutView.as_view(), name="about"),
    path('logout/', user_logout , name="logout")
]
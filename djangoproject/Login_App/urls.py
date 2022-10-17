from django.urls import path

from . import views

urlpatterns =  [
    path('Homepage/', views.HomePage),
    path('Indexpage/', views.IndexPage),
    path('all-student/', views.AllStudentDetails),
    path('student-details/<int:pk>', views.SingleStudentDetails),
]
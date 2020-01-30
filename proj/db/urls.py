from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.home, name="home")
    path('', views.emp_form, name="emp_form"),
    path('list/',views.list, name="list"),
    path('<int:id>/',views.emp_form, name ="employee_update"),
    path('delete/<int:id>',views.emp_delete, name ="emp_delete"),
]
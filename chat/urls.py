from django.urls import path,include
from .views import *



urlpatterns = [
    path("", home ,name='home'), 
    path("register/",user_create ,name='register' ), 
    path("tables_all/",tables ,name='tables_all' ), 
    path("comingtype/",comingtype ,name='comingtype' ), 
    path("delete/<int:id>/",delete ,name='delete' ), 
    path("update_sick/<int:id>/",update_sick ,name='update_sick' ), 

]

from django.urls import path,include
from .views import *



urlpatterns = [
    path("", home ,name='home'), 
    path("register/",user_create ,name='register' ), 
    path("tables_all/",tables ,name='tables_all' ), 
    path("comingtype/",comingtype ,name='comingtype' ), 
    path("delete/<int:id>/",delete ,name='delete' ), 
    path("delete1/<int:id>/",delete1 ,name='delete1' ), 
    path("delete2/<int:id>/",delete2 ,name='delete2' ), 
    path("update_sick/<int:id>/",update_sick ,name='update_sick' ), 
    path("update_sick1/<int:id>/",update_sick1 ,name='update_sick1' ), 
    path("update_sick2/<int:id>/",update_sick2 ,name='update_sick2' ), 

]

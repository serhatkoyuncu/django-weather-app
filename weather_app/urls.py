from django.urls import path
from. views import delete_city, index

urlpatterns = [
   path('',index,name="home"),
   path('delete/<id>',delete_city,name="delete")
]
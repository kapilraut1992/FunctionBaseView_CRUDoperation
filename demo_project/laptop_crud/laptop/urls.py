from django.urls import path
from .views import laptop_info,show_data,update_data,delete_data

urlpatterns=[
    path('addlap/',laptop_info,name='laptop_add'),
    path('laptop_list/',show_data,name='laptop_list'),
    path('update/<int:id>/',update_data,name='update_data'),
    path('delete/<int:id>/',delete_data,name='delete_data'),
]
from django.urls import path

from api import views

urlpatterns = [

    # Using for UI entry
     path('',views.register_fun,name='reg'),
    path('reg',views.register_fun,name='reg'),

    # Useding for Backend Auto entry
    # path('',views.read_fun,name='data'),
    path('/api/data/',views.read_fun,name='data'),
    path('/api/merge/', views.merge_data, name='merge_data'),

]
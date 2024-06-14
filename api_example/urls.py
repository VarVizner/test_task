from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('upload_excel/', views.import_from_excel, name='upload_excel'),
    path('add/', views.add_element, name="add_element"),
    path('all/', views.view_elements, name='view_elements'),
    path('update/<int:code>/', views.update_element, name='update_element'),
    path('delete/<int:code>/', views.delete_element, name='delete_element')
]
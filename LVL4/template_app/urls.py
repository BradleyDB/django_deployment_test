from django.urls import path
from template_app import views

#for template tagging needs to be called app_name
app_name = 'template_app'


urlpatterns = [

    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),

]

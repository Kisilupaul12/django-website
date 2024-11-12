from django.urls import path

from Project1_app import views

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('chocolate/',views.chocolate,name='chocolate'),
    path('testimonial/',views.testimonial,name='testimonial')

]
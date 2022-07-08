from django.urls import path
from track import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('price/',views.price, name='price'),
    path('contact/',views.contact, name='contact'),
    path('track/<str:pk>',views.track, name='track'),
    path('adminified-form-003/',views.filler, name='filler'),
    path('modify_track/<str:pk>',views.modifytrack, name='modify'),
]

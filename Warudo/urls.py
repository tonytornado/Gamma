from django.urls import path

from Warudo import views

urlpatterns = [
    path('profiles', views.ProfileList.as_view(), name='profile-list'),
    path('profile/<slug:slug>', views.ProfileViewer.as_view(), name='cos-profile')
]

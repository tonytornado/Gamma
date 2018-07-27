from django.urls import path

from Warudo import views

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile-list'),
    path('<str:Name>', views.ProfileViewer.as_view(), name='profile')
]

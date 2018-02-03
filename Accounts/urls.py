from django.urls import path

from Accounts import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.Register, name='register'),
    # path('profile/', views.ProfileViewer, name='profile'),
]

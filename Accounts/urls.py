from django.urls import path

from Accounts import views

urlpatterns = [
    path('<str:Name>/', views.AccountView.as_view(), name='user_profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register')
    # path('profile/', views.ProfileViewer, name='profile'),
]
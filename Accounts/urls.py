from django.urls import path

from Accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<int:pk>/', views.AccountView.as_view(), name='user_profile'),
    # path('profile/', views.ProfileViewer, name='profile'),
]
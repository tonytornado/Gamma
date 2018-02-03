from django.urls import path, include

from Warudo import views

urlpatterns = [
    path('profile/', include([
        path('', views.ProfileList.as_view(), name='device-list'),
        path('<int:pk>', include([
            path('', views.ProfileViewer.as_view(), name='profile')
        ]))
    ])),
]

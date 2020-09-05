from knox import views as knox_views
from django.urls import path
from myapp import views
from .views import RegisterAPI
from .views import LoginAPI

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('trackker/',views.Trackker,name='tracker'),
    path('checkout/',views.Checkout, name="checkout"),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('accounts/',views.Create_Account, name="account")
]

from django.urls import path
from .views import signup, logout_view, login_view, home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
]
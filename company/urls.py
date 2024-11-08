from django.contrib import admin
from django.urls import include, path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('signup',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/', views.logout_page,name='logout'),
    path('crud/',include('crud.urls')),
    
   
]
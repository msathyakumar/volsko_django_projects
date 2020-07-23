from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path('home',views.home_page_return),
    path("login",views.login_page),
    path('register',views.register_page),
    path('Details',views.info_page),
    path('logout',views.logout_page)
    
]

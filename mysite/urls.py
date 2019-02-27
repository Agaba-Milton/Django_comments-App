
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/accounts/login --> local
    #path('accounts/login/', auth_views.login, name='login'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # 127.0.0.1:8000/accounts/logout --> local
    #path('accounts/logout/', view=auth_views.logout, name='logout', kwargs={'next_page': 'post_list'}),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    path('', include('blog.urls')),
]

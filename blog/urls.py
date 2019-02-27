from django.urls import path
from . import views

urlpatterns = [

#post list
    path('', views.post_list, name='post_list'),

#post details
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

#new post
    path('post/new/', views.post_new, name='post_new'),

#post edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

#post delete
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

#post draft list
    path('drafts/', views.post_draft_list, name='post_draft_list'),

#publish post
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

#add comment
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

#remove comment
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

#Approve comment
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),

#sign up
    path('signup/', views.signup, name='signup'),

    path('login/', views.login, name='login'),
]
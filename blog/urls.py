from django.urls import path 
from . import views 

urlpatterns = [
	path('', views.index, name='blog_index'),
	path('content/<slug:slug>/', views.blog_detail, name='blog_detail'),
	path('signup/', views.signup, name='blog_signup'),
	path('signin/', views.signin, name='blog_signin'),
	path('logout/', views.signout, name='blog_signout'),
	path('admin/create/', views.create_post, name='create_post'),
	path('admin/<str:filter>/', views.blog_admin_index, name='blog_admin_index'),
	path('admin/modify/<slug:slug>', views.update_blog, name='update_blog'),
	path('admin/delete/<slug:slug>', views.delete_blog, name='delete_blog'),

]
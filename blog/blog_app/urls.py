from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='signup'),
    path('h', views.home, name='home'),
    path('c', views.create_post, name='create_post'),
    path('d/<int:post_id>', views.delete_post, name='delete_post'),

]

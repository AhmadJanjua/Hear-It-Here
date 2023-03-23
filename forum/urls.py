from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.browse_categories, name='categories'),
    path('<int:category_id>/', views.browse_posts, name='posts'),
    path('<int:category_id>/<int:post_id>/', views.view_post, name='view_post'),
    path('<int:category_id>/create/', views.create_post, name='create_post'),
    path('<int:category_id>/<int:post_id>/delete/', views.delete_post, name='delete_post'),

]
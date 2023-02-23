from django.urls import path

from projects import views


app_name = "projects"

urlpatterns = [
    path('', views.project_list, name='project-list'),
    path('<int:id>/', views.project_detail, name='project-detail'),
    path('add/', views.project_create, name='project_create'),
    path('<int:id>/change/', views.project_update, name='project-update'),
    path('<int:id>/delete/', views.project_delete, name='project-delete'),

    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent),
]
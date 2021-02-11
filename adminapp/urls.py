from django.urls import path

import adminapp.views as adminapp_views

app_name = 'adminapp'

urlpatterns = [
   path('',  adminapp_views.index, name='index'),
   path('admin-users-read/',  adminapp_views.admin_users_read, name='admin_users_read'),
   path('admin-users-create/',  adminapp_views.admin_users_create, name='admin_users_create'),
   path('admin-users-update/<int:id>/',  adminapp_views.admin_users_update, name='admin_users_update'),
   path('admin-users-delete/<int:id>/',  adminapp_views.admin_users_delete, name='admin_users_delete'),
   path('admin-active-user/<int:id>/',  adminapp_views.admin_active_user, name='admin_active_user'),


]

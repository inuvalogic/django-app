from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

from django.contrib import admin

admin.site.site_header = 'Admin CMS'
admin.site.index_title = 'Dashboard'
admin.site.site_title = 'Project Name'
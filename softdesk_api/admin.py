from django.contrib import admin

# Register your models here.

from .models import Project, Contributor, Issue, Comment

admin.site.register([Project, Contributor, Issue, Comment])

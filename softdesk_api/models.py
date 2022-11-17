from turtle import title
from django.db import models
from django.conf import settings

TYPES = [
    ('backend', 'Backend'),
    ('frontend', 'Frontend'),
    ('ios', 'iOS'),
    ('android', 'Android')
]

PERMISSIONS = [
    ('allowed', 'Allowed'),
    ('forbidden', 'Forbidden')
]

ROLES = [
    ('author', 'Auteur'),
    ('manager', 'Responsable'),
    ('creator', 'Créateur')
]

TAGS = [
    ('bug', 'Bug'),
    ('task', 'Tâche'),
    ('improvement', 'Amélioration')
]

PRIORITIES = [
    ('minor', 'Mineur'),
    ('high', 'Haute'),
    ('critical', 'Crutial')
]

STATUS = [
    ('pending', 'En attente'),
    ('in progress', 'En progression'),
    ('done', 'Terminé')
]

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(choices=TYPES, default='', max_length=50)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

class Contributor(models.Model):
    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, blank=True)
    permission = models.CharField(choices=PERMISSIONS, default='', max_length=50)
    role = models.CharField(choices=ROLES, default='',max_length=50)


class Issue(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tag = models.CharField(choices=TAGS, default='', max_length=50)
    priority = models.CharField(choices=PRIORITIES, default='', max_length=50)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='', max_length=50)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, related_name='author_user_id', on_delete=models.CASCADE, blank=True)
    assignee_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, related_name='assignee_user_id', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    issue_id = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

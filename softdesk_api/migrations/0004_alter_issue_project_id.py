# Generated by Django 4.1.2 on 2022-11-17 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_api', '0003_alter_contributor_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='softdesk_api.project'),
        ),
    ]

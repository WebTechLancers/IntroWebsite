# Generated by Django 4.2.1 on 2023-05-28 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.features'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images', to='projects.imageexamples'),
        ),
    ]
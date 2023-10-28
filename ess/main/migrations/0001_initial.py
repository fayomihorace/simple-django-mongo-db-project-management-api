# Generated by Django 3.2 on 2023-10-28 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, help_text='Task deadline', null=True)),
                ('assigned_user', models.ForeignKey(help_text='User responsible of the task', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('logo', models.FileField(blank=True, null=True, upload_to='logos')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('owner_name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('tasks', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
                ('users', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
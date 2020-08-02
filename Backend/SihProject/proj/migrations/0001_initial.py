# Generated by Django 3.0.6 on 2020-07-27 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0)),
                ('lat', models.FloatField(default=80.0)),
                ('lon', models.FloatField(default=50.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('reviewed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NGOUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mob', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('contributions', models.PositiveIntegerField(default=0)),
                ('reg_num', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserContributionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.PositiveSmallIntegerField(default=0)),
                ('workCompleted', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='13232', max_length=50)),
                ('lat', models.FloatField(default=80.0)),
                ('lon', models.FloatField(default=50.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('animals', models.PositiveSmallIntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.ActiveArea')),
                ('contributinguser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
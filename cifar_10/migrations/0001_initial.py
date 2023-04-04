# Generated by Django 4.1.7 on 2023-04-02 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeuralModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.FileField(upload_to='models/%Y/%m/%d')),
                ('model_type', models.CharField(max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('predicted', models.BooleanField(default=False)),
                ('model_prediction', models.CharField(max_length=25, null=True)),
                ('accuracy', models.FloatField(blank=True, null=True)),
                ('info_from_user', models.CharField(max_length=25, null=True)),
                ('session_key', models.CharField(blank=True, max_length=150, null=True)),
                ('model_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cifar_10.neuralmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
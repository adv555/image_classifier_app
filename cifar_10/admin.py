from django.contrib import admin
from .models import NeuralModel, ImageManager

# Register your models here.

admin.site.register(NeuralModel)
admin.site.register(ImageManager)
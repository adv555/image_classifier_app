from django import forms
from .models import NeuralModel, ImageManager


class UploadFile(forms.Form):
    choose_file = forms.ImageField(widget=forms.FileInput(attrs={'class': 'upload_file'}))
    # model = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'model_choice'}),
    #                                queryset=NeuralModel.objects.all(), initial=1)

    # model = forms.CharField(widget=forms.TextInput(attrs={'class': 'model_choice'}))
    # class Meta:
    #     model = ImageManager
    #     fields = ('file_name',)

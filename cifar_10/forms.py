from django import forms
from .models import NeuralModel, ImageManager


class UploadFile(forms.Form):
    choose_file = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'upload_file block w-full text-lg text-gray-900 border border-gray-300 rounded-lg '
                        'cursor-pointer bg-[#d0e4da]  focus:outline-none'}))
    # model = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'model_choice'}),
    #                                queryset=NeuralModel.objects.all(), initial=1)

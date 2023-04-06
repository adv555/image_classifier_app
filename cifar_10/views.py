from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import default_storage
from cloudinary_storage.storage import MediaCloudinaryStorage
from .forms import UploadFile
from .models import NeuralModel, ImageManager
from .keras_model import image_classify
from django.utils import timezone
from datetime import datetime, timedelta


class IndexView(View, LoginRequiredMixin):
    template_name = 'pages/classifier.html'
    form_class = UploadFile
    context = {}

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        self.context.update({'form': self.form_class})
        image = ImageManager.objects.filter(session_key=request.session.session_key).last()

        if image:
            self.context.update({'image': image})
            self.context.update({'result': image.model_prediction})
            self.context.update({'accuracy': image.accuracy})

        if self.context.get('image'):
            difference = datetime.now(timezone.utc) - image.uploaded_at
            if difference > timedelta(minutes=1):
                self.context.update({'image': None})
                self.context.update({'result': None})
                self.context.update({'accuracy': None})

        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):

        file = request.FILES['choose_file']
        file_name = file.name
        file_path = default_storage.save(file_name, file)
        file_url = default_storage.url(file_path)

        if isinstance(default_storage, MediaCloudinaryStorage):
            file_name = file_url
        else:
            file_name = file_path

        model = 1
        neural_model = NeuralModel.objects.get(pk=model)
        model_path = neural_model.model_name.name

        document = ImageManager.objects.create(file_name=file_name,
                                               model_type=neural_model,
                                               session_key=request.session.session_key,
                                               user_id=request.user.id
                                               )
        document.save()
        document_path = file

        result = image_classify(document_path, model_path)


        if result != ["Invalid photo"]:
            document.model_prediction = result[0]
            document.accuracy = result[1]
            document.predicted = True
            document.save()

        return redirect('cifar_10:cifar_10')
        # return redirect('frontend:classifier')


class HistoryView(LoginRequiredMixin, View):
    template_name = 'pages/history.html'
    model = ImageManager

    def get(self, request, *args, **kwargs):
        images = self.model.objects.filter(user_id=request.user.id).order_by('-uploaded_at')[:8]
        return render(request, self.template_name, context={'title': 'Predictions history', 'images': images})


def show_all_images(request):
    images = ImageManager.objects.filter(user_id=request.user.id).order_by('-uploaded_at')
    return render(request, 'pages/history.html', context={'title': 'Predictions history', 'images': images})


def clear_history(request):
    images = ImageManager.objects.filter(user_id=request.user.id).delete()
    return redirect('cifar_10:history')


def delete_image(request, pk):
    image = ImageManager.objects.get(pk=pk)
    image.delete()
    return redirect('cifar_10:history')

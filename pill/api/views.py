from . import models
from .models import FileUpload
from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect, request
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, FormView
from django.shortcuts import redirect
import asyncio
import time
from pill.load import LoadConfig
from datetime import datetime
from api.prediction import shape_pred
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

model = LoadConfig.model

class ImageUploadView(CreateView):
    model = FileUpload
    fields = "__all__"
    success_url= reverse_lazy('api:img_list')
    template_name='api/form.html'

    def form_valid(self, form):
        images = form.save(commit=False)
        images.save_files = self.request.FILES['file']
        images.save()
        media = FileUpload.objects.get(save_files=images.save_files).save_files.path
        images.predict_shape = asyncio.run(shape_pred(media, model))
        images.predict_color = "None"
        images.save()
        return super().form_valid(form)

class ImageDetailView(TemplateView) :
    template_name = "api/result.html"
    def get_context_data(self, **kwargs: str) :
        context =  super().get_context_data(**kwargs)
        context['images'] = FileUpload.objects.all()
        return context
    
def tab_test(request) :
    return render(request, "api/tab.html")

def test(request) :
    return render(request, "api/cam_test.html")
# class PredictView(View):
#     def post(self, request, * args, **kwargs):
#         # Load the deep learning model
#         model = tf.keras.models.load_model('model.h5')

#         # Prepare the input image
#         image = request.FILES['image']
#         preprocessed_image = preprocess_image(image)
#         input_tensor = tf.expand_dims(preprocessed_image, axis=0)

#         # Make predictions with the model
#         predictions = model.predict(input_tensor)

#         # Pass the predictions to the template
#         return render(request, 'prediction.html', {'predictions': predictions})


    
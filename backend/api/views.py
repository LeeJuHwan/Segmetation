from django.db.models import Q
from . import models
from django.contrib import messages
from .models import FileUpload, User, DrugInfo, DrugInfoEfcy, DrugMaterial
from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect, request, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.shortcuts import redirect
import asyncio
import time
from pill.load import LoadConfig
from datetime import datetime
import os
import cv2
import numpy as np
import ast
import requests
from bs4 import BeautifulSoup
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

class ImageUploadView(CreateView):
    model = FileUpload
    fields = "__all__"
    success_url= reverse_lazy('api:img_list')
    template_name='api/form.html'

    def form_valid(self, form):
        start_time = time.time()
        images = form.save(commit=False)
        try : 
            images.save_files = self.request.FILES['file']
            images.save()
        except :
            return self.form_invalid(form)
        pk = images.id
        print("pk : ", pk)
        media = FileUpload.objects.get(save_files=images.save_files).save_files.path
        res = LoadConfig.pill_module.predict_shorten(media)

        # item_name = [name[1] for index, _ in enumerate(res) for name in res[index][2]]
        print(f"알약 예측 소요 시간 : {time.time() - start_time}")

        # can't use comprehension cases need seperator 
        item_name = []
        for index, _ in enumerate(res) :
            tmp = []
            for name in res[index][2]:
                tmp.append(name[1])
            item_name.append(tmp)
        User.objects.create(id = pk, data_result = item_name, label ="None")
        os.mkdir(f"/home/lab06/Segmetation/backend/static/img/temp/{pk}")
        os.mkdir(f"/home/lab06/Segmetation/backend/static_root/img/temp/{pk}")
        temp_path = f"/home/lab06/Segmetation/backend/static/img/temp/{pk}/"
        root_temp_path = f"/home/lab06/Segmetation/backend/static_root/img/temp/{pk}/"

        for i,j in enumerate(res) :
            print(i, "indexing")
            cv2.imwrite(f"{root_temp_path}temp{i}.jpg",res[i][0])
            cv2.imwrite(f"{temp_path}temp{i}.jpg",res[i][0])
            images.predict_shape = res[i][1]["shape"]
            images.predict_color = res[i][1]["color"]
            images.result = res[i][2]
            images.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, error="사진을 추가 한 뒤 등록 버튼을 눌러주세요."), status=400)

    def get_success_url(self):
        return reverse('api:img_list', kwargs={'pk':self.object.id})

class ImageDetailView(TemplateView) :
    template_name = "api/search_result.html"
    model = User
    def get_context_data(self, **kwargs: str) :
        context = super().get_context_data(**kwargs)
        print("GET PK :", self.kwargs.get("pk"))
        pk = self.kwargs.get("pk")
        queryset = User.objects.filter(id=pk).values_list("data_result")
        qs = [i[0] for i in queryset]
        qs = ast.literal_eval(qs[0])
        context["user"] = qs
        context["pk"] = pk

        return context

class TabView(TemplateView) :
    template_name = "api/tab.html"

class Search(ListView) :
    template_name='api/search_word.html'
    def get_queryset(self):
        query = self.request.GET.get('search-word')
        object_list = DrugInfo.objects.filter(
            Q(ITEM_NAME__icontains=query)
        )
        return object_list

def detail_fbv(request) :
    # queryset
    name = request.GET.get("item_name")
    seq = DrugInfo.objects.filter(ITEM_NAME = name).values_list("ITEM_SEQ")
    item_seq = str(seq[0][0])
    try : 
        method_queryset = DrugInfoEfcy.objects.filter(itemSeq = item_seq).values()[0]
        maetrial_queryset = DrugMaterial.objects.filter(ITEM_SEQ = item_seq).values()[0]
    except IndexError : 
        method_queryset = {}
        maetrial_queryset = {}
    
    shape_queryset = DrugInfo.objects.filter(ITEM_SEQ = item_seq).values()[0]

    #template context
    info_dict = {}
    info_dict["img_file"] = name + ".jpg"

    # shape
    info_dict["name"] = shape_queryset.get("ITEM_NAME", "알 수 없음")
    info_dict["seq"] = shape_queryset.get("ITEM_SEQ", "알 수 없음")
    info_dict["comp"] = shape_queryset.get("ENTP_NAME", "알 수 없음")
    info_dict["print_front"] = shape_queryset.get("PRINT_FRONT", "알 수 없음")
    info_dict["print_back"] = shape_queryset.get("PRINT_BACK", "알 수 없음")
    info_dict["color"] = f'{shape_queryset.get("COLOR_CLASS1", "알 수 없음")} {shape_queryset.get("COLOR_CLASS2", "알 수 없음")}'
    info_dict["shape"] = shape_queryset.get("DRUG_SHAPE", "알 수 없음")
    # material
    info_dict["material"] = maetrial_queryset.get("MATERIAL_NAME", "알 수  없음")
    info_dict["class_no"] = maetrial_queryset.get("CLASS_NO", "")

    # use_method
    info_dict["usage"] = method_queryset.get("efcyQesitm", "알 수 없음").replace("<p>", "").replace("</p>", "").replace("<br />", "")
    info_dict["method"] = method_queryset.get("useMethodQesitm", "알 수 없음").replace("<p>", "").replace("</p>", "").replace("<br />", "")
    info_dict["attention"] = method_queryset.get("atpnQesitm", "알 수 없음").replace("<p>", "").replace("</p>", "").replace("<br />", "")
    info_dict["deposit"] = method_queryset.get("depositMethodQesitm", "알 수 없음").replace("<p>", "").replace("</p>", "").replace("<br />", "")

    return render(request, "api/render_detail.html", {"info_dict" : info_dict})



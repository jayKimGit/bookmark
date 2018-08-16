from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Bookmark
from django.urls import reverse_lazy

# Create your views here.
# view 종류 : 함수형, 클래스형
# 장고 목적 ? : 귀찮은거 하기 싫어서...
# 클래스형 : 자주 쓰는 기능을 상속받아서 간단하게 생성

# list view
class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 렌더링할 템플릿 파일이 지정이 되어 있습니다.
    # bookmark/bookmark_list.html

class BookmarkCreateView(CreateView):
    model = Bookmark
    # 입력받을 필드 목록
    # default : _form
    template_name_suffix = '_create'
    fields = ['site_name', 'url']
    # get_absolute_url 을 자동으로 호출함
    success_url = reverse_lazy('list')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name_suffix = '_update'
    fields = ['site_name', 'url']
    #success_url = reverse_lazy('detail')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'

'''
def list(request):
    return HttpResponse("List")
def write(request):
    return HttpResponse("Write")

def update(request):
    return HttpResponse("Update")

def delete(request):
    return HttpResponse("Delete")
'''
from django.urls import path
from .views import *
# from . import views

# url 이름을 가지고 패턴을 찾고자 할때 namespace를 사용하려면 app_name이 필수
app_name = 'bookmark'
urlpatterns = [
    # path('', list, name='list'),
    # re_path(regexp,'',''),
    # 함수형뷰 : 함수 이름만
    # 클래스형뷰 : 클래스 이름.as_view()
    path('list/', BookmarkListView.as_view(), name='list'),
    path('write/', BookmarkCreateView.as_view(), name='write'),
    # <1:2> : 1 - data type, 2 - data name
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),


#    path('list/', views.list, name='list'),
#    path('write/', views.write, name='write'),
#    path('update/', views.update, name='update'),
#    path('delete/', views.delete, name='delete'),

]
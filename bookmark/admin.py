from django.contrib import admin
from .models import Bookmark

# Register your models here.

# Todo : 관리자 페이지 커스터마이징
admin.site.register(Bookmark)

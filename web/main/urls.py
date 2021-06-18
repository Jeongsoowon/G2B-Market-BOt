from django.urls import path
from django.contrib import admin
from .views import *

app_name ='main'
urlpatterns = [
        path('admin/', admin.site.urls),
        # 웹사이트의 첫화면은 index 페이지이다. + URL 이름은 index 이다.
        path('', index, name='index'),
        # URL:80/blog에 접속하면 blog 페이지 + URL 이름은 blog dlek.
        path('blog/', blog, name = 'blog'),
        # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
        path('blog/<int:pk>', posting, name="posting")
]

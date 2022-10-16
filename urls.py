from django.contrib import admin
from django.urls import path
from pengertian.views import index
from jenis.views import index
from rumus.views import index
from soal.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pengertian/',index),
    path('jenis/',index),
    path('rumus/',index),
    path('soal/',index),

]

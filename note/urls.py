
from django.urls import path
from . import views
#from django.conf.urls import include


urlpatterns = [

    path('', views.index, name='home'),
    path('note', views.note, name='note'),
    #path('tinymce/', include('tinymce.urls')),
    #path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

from django.urls import path, re_path
from .views import Index
from django.views.generic import TemplateView

app_name = 'frontend'
urlpatterns = [
    path('', Index.as_view(), name='all'),
    path('search/', Index.as_view()),
   
    ]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
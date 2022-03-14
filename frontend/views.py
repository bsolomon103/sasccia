
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

# Create your views here.

class Index(LoginRequiredMixin, View):
    template = 'index.html'
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
     
        return render(request, self.template)
        
    
    
from django.urls import path, include
from .views import SummaryView, GetClientView, GetCSRFTokenView,LoginView, LogoutView, CheckAuthenticatedView



urlpatterns = [
    path('all', SummaryView.as_view()),
    path('get-client', GetClientView.as_view()),
    path('csrf_cookie',GetCSRFTokenView.as_view()),
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
  
    ]
from django.shortcuts import render
from rest_framework import generics, status
from .models import Client,Ethnicity, PrimarySupportReason, RouteOfAccess, ServiceType
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Avg, Min, Max, Count
from django.http import HttpResponse
#from .requestcount import requestCount
from .healthprofile import health_profile
import clients.functions as funcs
import clients.search as search
from rest_framework.decorators import action
from .serializers import ClientSerializer, GetClientSerializer, LoginSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout




@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(GenericAPIView):
    def get(self,request,format=None):
        user = self.request.user
        try:
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                return Response({'isAuthenticated':'success'})
            else: 
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error':'Something went wrong when checking authentication status'})
            
            
@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    #serializer_class = LoginSerializer
    def post(self, request, format=None):
        data = self.request.data
        username = data["username"]
        password = data['password']
            
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'success':'User authenticated', 'user':username})
        else:
            return Response({'error':'User Not Authenticated'})
        

class LogoutView(APIView):
    def post(self,request,format=None):
        try:
            logout(request)
            return Response({'success':'Logged Out'})
        except:
            return Response({'error':'Something went wrong try again'})
    

@method_decorator(csrf_protect, name='dispatch')
class SummaryView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        try:
            client_count = Client.objects.values_list('lasID',flat=True).order_by('lasID').distinct().count()
            # Ethnicity
            races = funcs.ethnicity()
            # PSR
            psrs = funcs.support_reasons()
            # Route Of Access
            routes = funcs.routesOfAccessCount()
            # Service Type
            servs = funcs.services()
            # Age
            age  = Client.objects.all().aggregate(Avg('age'))
            #Request Count
            request_count = funcs.request_count_month()
            #Outcomes
            outcome = funcs.outcomes_list()
            #Assessment Delta
            delta = funcs.assessment_delta()
            age_delta = funcs.age_assessmentDelta()
            # Days 
            start = Client.objects.all().aggregate(Min('requestStart'))
            end = Client.objects.all().aggregate(Max('requestStart'))
            timeframe = round((end['requestStart__max'] - start['requestStart__min']).days/365,2)
            health = health_profile()
            costs = funcs.health_costs()
            top_providers = funcs.providers()
            units = funcs.unit_cost()
            living_situation = funcs.acc_employment()
           
            data = {
                    'Total_Number_of_clients':client_count,
                    'Ethnicity_Distribution_Of_Clients': races, 
                    'Distribution_of_Service_Types': servs,
                    'Primary Support Reason': psrs,
                    'Routes Of Access' : routes,
                    'Timeframe' : timeframe,
                    'Request Count': request_count,
                    'Request Outcomes': outcome,
                    'Assessment Completion': delta,
                    'Assessment Completion_Age_Eligibility' : age_delta,
                    'Health Profile': health, 
                    'Health Costs': costs, 
                    'Top Providers': top_providers,
                    'Living Situation': living_situation,
                    'Fix':units
                    }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'error':'Summary Page API Error'})
        
        
@method_decorator(csrf_protect,name='dispatch')
class GetClientView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = GetClientSerializer
    def post(self, request, format=None):
        try:
            las_id = request.data['lasID']
            queryset = Client.objects.filter(lasID=las_id)
            basics = search.basics(queryset)
            ratio = search.request_service_ratio(queryset)
            #split = search.eligibility(queryset)
            psr = search.psr(queryset)
            #components = search.components(queryset)
            health = search.health_conditions(queryset)
            plan_type = search.plan_type(queryset)
            #delivery_mechanism = search.delivery_mechanism(queryset)
            particulars = search.service_particulars(queryset)
            eligibility = search.eligibility(queryset)
            deceased = search.deceased(queryset)
            data = {'Basics' : basics,
                    'Request_Service_Ratio': ratio,
                    'PSR' : psr,
                    'Health Conditions' : health, 
                    'Service Particulars' : particulars,
                    'Plan Type' : plan_type,
                    'Eligibility' : eligibility,
                    'Deceased' : deceased
            }
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':e})
            
        

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        return Response({'success':'CSRF Cookie set'})



        
        

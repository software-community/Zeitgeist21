from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from main.models import *
from .serializers import *
from users.serializers import *

# Create your views here.
class APIEvent(APIView):
  def get(self,request):
    events = Event.objects.all()
    eventsSER = EventSerializer(events, many=True)
    categorySER = UniqueCategorySerializer(events)
    typeSER = UniqueTypeSerializer(events)
    return Response({'categories':categorySER, 'types':typeSER, 'events':eventsSER.data})

def check_user_registered(users):
  arr = []
  for i in users:
    if not i.active:
      arr.append(i)
  return arr

def check_user_registered_error(users):
  check = check_user_registered(users)
  if len(check)!=0:
    userSER = UserSerializer(check, many=True)
    return Response({"Error":"User details not complete", "users":userSER.data}, status="461")
  return None

def check_zcode_error(zcodes):
  check = []
  for x in zcodes:
    if len(User.objects.filter(zcode=x))==0:
      check.append(x)
  if len(check)!=0:
    return Response({"Error":"Z-Codes not valid", "zcodes":check},status="463")
  return None

class APIEventRegisterApprove(APIView):
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self,request):
    event_id = request.data.get("event_id")
    event = Event.objects.filter(event_id=event_id)
    if len(event)==0:
      return Response({"Error":"Invalid event_id"}, status="460")
    
    user = request.user
    error = check_user_registered_error([user])
    if error!=None:
      return error
    # If already registered in that event -> error
      # return Response({"Error":"User already registered in this event"}, status="462")
    userSER = UserSerializer(user)
    eventSER = EventSerializer(event[0])
    return Response({'user':userSER.data,'event':eventSER.data})

class APIEventRegister(APIView):
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self,request):
    event_id = request.data.get("event_id")
    event = Event.objects.filter(event_id=event_id)[0]
    if event==None:
      return Response({"Error":"Invalid event_id"}, status="460")
    
    zcodes = request.data.get("zcodes")
    error = check_zcode_error(zcodes)
    if error!=None:
      return error

    users = User.objects.filter(zcode__in=zcodes)
    error = check_user_registered_error(users)
    if error!=None:
      return error
    # If already registered in that event -> error
      # return Response({"Error":"User already registered in this event"}, status="462")
    amount = event.registration_amount*len(zcodes)
    userSER = UserSerializer(users,many=True)
    eventSER = EventSerializer(event)
    return Response({'amount':amount,'users':userSER.data,'event':eventSER.data})

class APIEventPayment(APIView):
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self,request):
    payment_details = request.data.get("payment")

    event_id = request.data.get("event_id")
    event = Event.objects.filter(event_id=event_id)[0]
    if event==None:
      return Response({"Error":"Invalid event_id"}, status="460")
    
    zcodes = request.data.get("zcodes")
    error = check_zcode_error(zcodes)
    if error!=None:
      return error

    users = User.objects.filter(zcode__in=zcodes)
    error = check_user_registered_error(users)
    if error!=None:
      return error
    # If already registered in that event -> error
      # return Response({"Error":"User already registered in this event"}, status="462")
    amount = event.registration_amount*len(zcodes)
    userSER = UserSerializer(users,many=True)
    eventSER = EventSerializer(event)
    return Response({'amount':amount,'users':userSER.data,'event':eventSER.data})
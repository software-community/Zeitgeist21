from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from main.models import *
from .serializers import *
from users.serializers import *
import json

# Create your views here.
class APIEvent(APIView):
  type = None
  def get(self,request):
    if self.type=='tech':
      events = Event.objects.all().filter(category__type='tech')
    elif self.type=="cult":
      events = Event.objects.all().filter(category__type='cult')
    else:
      events = Event.objects.all()
    eventsSER = EventSerializer(events, many=True, context={"request":request})
    categorySER = UniqueCategorySerializer(events)
    typeSER = UniqueTypeSerializer(events)
    return Response({'categories':categorySER, 'types':typeSER, 'events':eventsSER.data})

def check_user_activated(users):
  arr = []
  for i in users:
    if not i.active:
      arr.append(i)
  return arr

def check_user_activated_error(users):
  check = check_user_activated(users)
  if len(check)!=0:
    userSER = UserSerializer(check, many=True)
    return Response({"Error":"User details not complete", "users":userSER.data}, status="461")
  return None

def check_user_already_registered_error(users, event_id):
  check = []
  for user in users:
    participation = json.loads(user.participation)
    for x in participation:
      if x["event"]==event_id:
        check.append(user)
        break
  if len(check)!=0:
    userSER = UserSerializer(check, many=True)
    return Response({"Error":"User already registered in this event", "users":userSER.data}, status="462")
  return None

def check_zcode_error(zcodes):
  check2 = []
  for x in zcodes:
    if x in check2:
      return Response({"Error":"Duplicate entries present"},status="465")
    check2.append(x)

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
    error = check_user_activated_error([user])
    if error!=None:
      return error
    
    error = check_user_already_registered_error([user], event_id)
    if error!=None:
      return error

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

    error = check_user_activated_error(users)
    if error!=None:
      return error
    
    error = check_user_already_registered_error(users, event_id)
    if error!=None:
      return error

    amount = event.registration_amount*len(zcodes)
    userSER = UserSerializer(users,many=True)
    eventSER = EventSerializer(event)
    return Response({'amount':amount,'users':userSER.data,'event':eventSER.data})

class APIEventPayment(APIView):
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self,request):
    payment_details = request.data.get("payment")

    # Save in payment model

    event_id = request.data.get("event_id")
    event = Event.objects.filter(event_id=event_id)[0]
    if event==None:
      return Response({"Error":"Invalid event_id"}, status="460")
    
    zcodes = request.data.get("zcodes")
    error = check_zcode_error(zcodes)
    if error!=None:
      return error

    users = User.objects.filter(zcode__in=zcodes)

    error = check_user_activated_error(users)
    if error!=None:
      return error

    error = check_user_already_registered_error(users, event_id)
    if error!=None:
      return error

    amount = event.registration_amount*len(zcodes)
    # If payment amount != amount 
      # return Response({"Error":"Payment amount not valid"}, status="464")

    # add event in users participation
    for user in users:
      current = user.participation
      current = json.loads(current)
      current.append({"event":event_id,"payment_id":"123"})
      current = json.dumps(current)
      user.participation = current
      user.save()

    userSER = UserSerializer(users,many=True)
    eventSER = EventSerializer(event)
    return Response({'detail':'Registered','amount':amount,'users':userSER.data,'event':eventSER.data})
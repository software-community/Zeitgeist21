from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from main.models import *
from .serializers import *
from users.serializers import *

# Create your views here.

class APIAccountInfo(APIView):
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self,request):
    user = request.user
    userSER = UserSerializerFullData(user)
    return Response(userSER.data)

class APIAccountInfoUpdate(APIView):
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self,request):
    user = request.user
    data = request.data

    if user.active == False:
      print(data.get("college"))
      if data.get("mobile")==None or data.get("college")==None or data.get("city")==None or data.get("mobile")=="" or data.get("college")=="" or data.get("city")=="":
        return Response({"Error":"Incomplete details"}, status="481")
      user.mobile = data.get("mobile")
      user.college = data.get("college")
      user.city = data.get("city")
      user.active = True
      user.save()
    else:
      for x in data:
        if data[x]!="" and data[x]!=None:
          setattr(user,x,data[x])
      user.save()

    userSER = UserSerializerFullData(user)

    return Response(userSER.data)
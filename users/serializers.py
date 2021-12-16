from rest_framework import serializers
from users.models import *
import json

class UserSerializer(serializers.ModelSerializer):
  full_name = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ['first_name','last_name','full_name','email','mobile','zcode']

  def get_full_name(self, obj):
    full_name = '{} {}'.format(obj.first_name, obj.last_name).strip()
    if full_name=="":
      full_name=obj.username
    return full_name

class UserSerializerFullData(serializers.ModelSerializer):
  full_name = serializers.SerializerMethodField()
  participation = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ['first_name','last_name','full_name','email','mobile','zcode','college','city','participation','total','active']

  def get_full_name(self, obj):
    full_name = '{} {}'.format(obj.first_name, obj.last_name).strip()
    if full_name=="":
      full_name=obj.username
    return full_name

  def get_participation(self, obj):
    return json.loads(obj.participation)
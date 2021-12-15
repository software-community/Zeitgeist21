from rest_framework import serializers
from users.models import *

class UserSerializer(serializers.ModelSerializer):
  full_name = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ['first_name','last_name','email','full_name','mobile','zcode']

  def get_full_name(self, obj):
    full_name = '{} {}'.format(obj.first_name, obj.last_name).strip()
    if full_name=="":
      full_name=obj.username
    return full_name
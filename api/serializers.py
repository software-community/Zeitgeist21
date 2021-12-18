from rest_framework import serializers
from main.models import *
from django.templatetags.static import static

def get_absolute_static_url(request, path):
  url = request.scheme + "://" + request.get_host() + static(path)
  return url

class EventCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = EventCategories
    fields = ['name','type']

class EventSerializer(serializers.ModelSerializer):
  category = EventCategorySerializer(many=False, read_only=True)
  image = serializers.SerializerMethodField()

  class Meta:
    model = Event
    fields = ['event_id', 'name', 'category', 'description', 'event_type', 'image', 'rulebook', 'registration_amount']
  
  def get_image(self, obj):
    request = self.context.get('request')
    link = get_absolute_static_url(request, "main/img/events/" + obj.image)
    return link

def UniqueCategorySerializer(events):
  arr=[]
  for x in events:
    if x.category.name not in arr:
      arr.append(x.category.name)
  return arr
  

def UniqueTypeSerializer(events):
  arr=[]
  for x in events:
    if x.category.type not in arr:
      arr.append(x.category.type)
  return arr
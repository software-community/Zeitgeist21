from rest_framework import serializers
from main.models import *

class EventCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = EventCategories
    fields = ['name','type']

class EventSerializer(serializers.ModelSerializer):
  category = EventCategorySerializer(many=False, read_only=True)
  class Meta:
    model = Event
    fields = ['event_id', 'name', 'category', 'description', 'event_type', 'image', 'rulebook', 'registration_amount']

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
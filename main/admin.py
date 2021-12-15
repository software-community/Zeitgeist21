from django.contrib import admin
from main.models import *

# Register your models here.
class EventCategoriesAdmin(admin.ModelAdmin):
  list_per_page = 5000
  list_display = ['id','name','type']

admin.site.register(EventCategories, EventCategoriesAdmin)

class EventAdmin(admin.ModelAdmin):
  list_per_page = 5000
  list_display = ['id','event_id','name','category']

admin.site.register(Event, EventAdmin)
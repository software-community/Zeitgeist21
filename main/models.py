from django.db import models



# Create your models here.
class EventCategories(models.Model):
  name = models.CharField(max_length=100)
  TYPE_CHOICES = [('tech','Technical'),('cult','Cultural'),]
  type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='tech')

  class Meta:
    verbose_name = 'Event Category'
    verbose_name_plural = 'Event Categories'

  def __str__(self):
        return self.name + " - " + self.type


class Event(models.Model):
  event_id = models.CharField(max_length=10, blank=False, unique=True)
  name = models.CharField(max_length=100, blank=False)
  category = models.ForeignKey(EventCategories, on_delete=models.CASCADE, null=False)
  description = models.TextField()
  EVENT_TYPE_CHOICES = [('solo', 'Solo'),('group', 'Group'),]
  event_type = models.CharField(max_length=5, choices=EVENT_TYPE_CHOICES, default='solo')
  registration_amount = models.IntegerField()
  start_date_time = models.DateTimeField()
  end_date_time = models.DateTimeField()
  image = models.CharField(max_length=100)
  rulebook = models.URLField(max_length=560)

  class Meta:
    verbose_name = 'Event'
    verbose_name_plural = 'Events'

  def __str__(self):
    return self.event_id + " - " + self.name


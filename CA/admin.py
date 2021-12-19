from django.contrib import admin
from .models import RegistrationDetail

class RegistrationDetailsAdmin(admin.ModelAdmin):

    list_display = ['get_user_name', 'get_user_email', 'campusAmbassadorCode', 'collegeName', 'mobileNumber']
    def get_user_name(self, obj):
     return obj.user.first_name + ' ' + obj.user.last_name

    get_user_name.short_description = 'User Name'
    get_user_name.admin_order_field = 'user__first_name'

    def get_user_email(self, obj):
        return obj.user.email

    get_user_email.short_description = 'User Email'
    get_user_email.admin_order_field = 'user__email'

admin.site.register(RegistrationDetail,RegistrationDetailsAdmin)


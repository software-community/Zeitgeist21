from __future__ import print_function
from django.shortcuts import redirect, render
from django.http import request
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import RegistrationDetail
from django.core.mail import send_mail
from django.templatetags.static import static
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json,os
from django.template.loader import render_to_string


def mainPage(request):
    return render(request, 'CA/main.html')


@login_required
def registerPage(request):
    try:
        prev_registration_details = RegistrationDetail.objects.get(user=request.user)
    except RegistrationDetail.DoesNotExist:
        prev_registration_details = None

    if prev_registration_details:
        return render(request, 'CA/register.html', {"msg":"You have already registered for this program.","det":prev_registration_details})
    request.user.email = SocialAccount.objects.get(
        user=request.user).extra_data.get("email")
    request.user.save()
    if request.method == "POST":
        campus_ambassador_registration_details_form = CampusAmbassadorRegistrationDetailsForm(
            request.POST)
        if campus_ambassador_registration_details_form.is_valid():
            new_campus_ambassador_registration = campus_ambassador_registration_details_form.save(
                commit=False)
            new_campus_ambassador_registration.user = request.user
            new_campus_ambassador_registration.campusAmbassadorCode = (
               "Z22-CA"+ str(request.user.id).zfill(4))
            # new_campus_ambassador_registration.save()
            send_mail(
                "Successful Registration for Campus Ambassador program for Zeitgeist'22",
                from_email='zeitgeist.pr@iitrpr.ac.in',
                message='',
                recipient_list=[request.user.email],
                fail_silently=False,
                html_message=render_to_string('CA/register_mail.html', {'user': request.user, 'det':new_campus_ambassador_registration, 'link':request.get_host() + static('CA/files/ca_policy_z22.pdf')})
            )
            updateCAgoogleSheet(request,new_campus_ambassador_registration)
            return render(request, 'CA/register.html', {"msg":"You have registered yourself successfully. For future reference, you are expected to remember this code.","det":new_campus_ambassador_registration})
    else:
        campus_ambassador_registration_details_form = CampusAmbassadorRegistrationDetailsForm()

    return render(request, 'CA/register.html',
                  {'form': campus_ambassador_registration_details_form})


def updateCAgoogleSheet(request,new_campus_ambassador_registration):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    credentials = None
    print(json.loads(os.environ.get('CA_SHEET')))
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(os.environ.get('CA_SHEET')), scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1NirhlgJ8WLRp_-aMsa8yEWCnJGLt-vTDZEORjmZvhp8'

    service = build('sheets', 'v4', credentials=credentials)
    body = {'values': [[request.user.first_name + ' ' + request.user.last_name, request.user.email, new_campus_ambassador_registration.campusAmbassadorCode,
                        new_campus_ambassador_registration.collegeName, str(new_campus_ambassador_registration.mobileNumber), new_campus_ambassador_registration.whyInterested, new_campus_ambassador_registration.pastExperience]]}
    service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                           range="Sheet1!A2", valueInputOption="RAW", body=body).execute()


def contactUs(request):
    return render(request, 'CA/contact.html')


def aboutUs(request):
    return render(request, 'CA/about.html')

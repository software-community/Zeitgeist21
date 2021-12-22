from django.shortcuts import render

# from TSP.methods import get_paid_details, payment_request

def TspHome(request):
    return render(request, 'TSP/index.html')
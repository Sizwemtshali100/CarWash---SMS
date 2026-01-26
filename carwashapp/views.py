from django.shortcuts import render, redirect, get_object_or_404
from . models import VehicleModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.conf import settings
from . SMS import send_sms
from . forms import VehicleForm
from . testing import testingMessage


# Create your views here.
def home(request):
    VehicleList = VehicleModel.objects.all()
    return render(request, 'home.html',
                  {
                      'VehicleList':VehicleList
                  })

def CarWashApplication(request):
    myVehicleLog = VehicleForm()
    if request.method == 'POST':
        myVehicleLog = VehicleForm(request.POST)
        if myVehicleLog.is_valid():    
            myVehicleLog.save()
            return redirect('home')
    return render(request, 'VehicleWashForm.html',
                  {'myVehicleLog':myVehicleLog})
    

def VehicleWashDetails(request, list_id):
    TheVehicleDetails = VehicleModel.objects.get(id=list_id)
    TheVehicleDetails_1 = get_object_or_404(VehicleModel, id=list_id)
    myMessage = None

    if request.method == 'POST':
        phone_number = TheVehicleDetails_1.ThePhoneNumber    

        sms_text = (
            f"Hello {TheVehicleDetails_1.TheDriverName}, you {TheVehicleDetails_1.TheVehicleMake} is ready"
        )
    
        status_code, response = send_sms(phone_number, sms_text)
        
        if status_code == 202:
            return redirect("home")
        else:
            myMessage = f"not sent {response}"

    return render(request, 'TheVehicleDetails.html',
                    {
                        'TheVehicleDetails_1':TheVehicleDetails_1,
                        'myMessage':myMessage,
                        'TheVehicleDetails':TheVehicleDetails
                    })


def LoginPage(request):
    if request.method == 'POST':
        TheUsername = request.POST['username']
        ThePassword = request.POST['password']
        TheUser = authenticate(request, username=TheUsername, password=ThePassword)
        if TheUser:
            login(request, TheUser)
            return redirect('home')    
    return render(request, 'LoginPage.html')

def RegistrationPage(request):
    UserCreate = UserCreationForm()
    if request.method == 'POST':
        UserCreate = UserCreationForm(request.POST)
        if UserCreate.is_valid():
            UserCreate.save()
        return redirect('LoginPage')
    return render(request, 'RegistrationPage.html',
                  {'UserCreate': UserCreate}
                  )

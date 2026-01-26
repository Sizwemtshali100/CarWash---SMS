from . models import VehicleModel
from django import forms
from django.forms import ModelForm

class VehicleForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['TheVehicleMake', 'TheDriverName',
                'TheColor', 'TheRegistrations',
                 'ThePhoneNumber']
                # 'TheStatus'
      
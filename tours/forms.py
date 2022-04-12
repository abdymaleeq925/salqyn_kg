from django import forms
from .models import TourBooking


class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ["place_count", "mobile", "notice"]
        widgets = {
            "place_count": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "mobile": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "notice": forms.TextInput(attrs={
                "class": "form-control"
            })
        }
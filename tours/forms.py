from django import forms
from .models import TourBooking, RegularTour


class TourBookingForm(forms.ModelForm):
    regular_tour = forms.ModelChoiceField(
        queryset=RegularTour.objects.filter(status=RegularTour.TOUR_STATUS_WAITING),
        widget=forms.Select(attrs={"class": "form-control"})
                                          )

    class Meta:
        model = TourBooking
        fields = ["regular_tour", "place_count", "mobile", "notice"]
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

from django import forms
from .models import Track

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['track_no', 'ship_date', 'location_code', 'weight' , 'del_date', 'ship_type','order_no','final_des']

class UpdateTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['track_no', 'ship_date', 'location_code', 'del_date', 'ship_type','status','order_no','final_des']
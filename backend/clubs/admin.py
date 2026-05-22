from django.contrib import admin
from django import forms
from .models import Club, ClubGalleryImage

class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        widgets = {
            'time' : forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
        
@admin.register(Club)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

admin.site.register(ClubGalleryImage)

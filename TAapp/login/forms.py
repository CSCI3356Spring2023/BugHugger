from django import forms
from login.models import Prof_profile, Stud_profile, Admin_profile

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Admin_profile
        fields = '__all__'
        exclude = ['user']
class ProfProfileForm(forms.ModelForm):
    class Meta:
        model = Prof_profile
        fields = '__all__'
        exclude = ['user']

class StudProfileForm(forms.ModelForm):
    class Meta:
        model = Stud_profile
        fields = '__all__'
        exclude = ['user']
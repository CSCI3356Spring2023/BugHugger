from django import forms
from view_apps.models import Semester

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'
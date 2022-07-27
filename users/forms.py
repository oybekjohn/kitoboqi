from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

# passwordni hashlash uchun ushbu save function yozildi
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
    

'''
# AuthenticationForm da tayyor borligi uchun bu form kerak emas
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)


# bu method yordamida manually datalarni tekshilishimiz mumkin cleaned_data bn
# lekin AuthenticationForm tayyor metodi yaratilgan bo'lib
# uni views da tayyor chaqirib ishlatamiz, u toliq validate qiberadi malumotlarni
# buni yozishga hojat qolmaydi

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

'''

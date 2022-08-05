from django import forms
from users.models import CustomUser

# from django.core.mail import send_mail


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

# passwordni hashlash uchun ushbu save function yozildi
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

# # email yuborish   bu signalga yozildi
#         if user.email:
#             send_mail(
#                 "Welcome to Kitob O'qi project!",
#                 f"Hi { user.username }, This is test message from our project.",
#                 "tempkitob@gmail.com",
#                 [user.email]
#             )

        return user
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', "email", "profile_picture"]

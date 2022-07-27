from urllib import response
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):

# ro'yxatdan muvaffaqiyatli o'tganligiga test
    def test_registration(self):
        self.client.post(
            reverse("users:register"), 
            data={
            'username': 'aka',
            'first_name': 'aka',
            'last_name': 'aka',
            'email': 'aka@gmail.com',
            'password': 'aka',
            }
        )

        user = User.objects.get(username='aka')
        
        self.assertEqual(user.first_name, 'aka')
        self.assertEqual(user.last_name, 'aka')
        self.assertEqual(user.email, "aka@gmail.com")
        self.assertNotEqual(user.password, 'aka')
        self.assertTrue(user.check_password('aka'))

    
# majburiy poliyalarni test qilish
    def test_required_fields(self):
# responsega self yani request orqali reverse urelga data yuborish
# va uni viewdagi form context orqali qaysidir poliyasiga malumot berib xatolikni olish
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "aka",
                "email": "aka@gmail.com"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "Ushbu maydon to'ldirilishi shart.")
        self.assertFormError(response, "form", "password", "Ushbu maydon to'ldirilishi shart.")

# user email formati xato kiritganligiga test
    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "email": "invalid-email", # qandaydir string yuborib korilyabdi
                "username": "aka",
                "first_name": "aka",
                "last_name": "aka",
                "password" : "something",
            }
        )

        user_count_from_database = User.objects.count()

        self.assertEqual(user_count_from_database, 0)
        self.assertFormError(response, "form", "email", "To'g'ri elektron pochta manzilini kiriting.")

# userlarni unique ekanligini tekshiramiz
    def test_user_uniqeu(self):
        # avval foydalanuvchi qo'shamiz chunki test qilishda bazadan olmaydi, o'zi yangi baza yaratib test qiladi
        addNew_user = User.objects.create(username="aka", first_name="aka")
        addNew_user.set_password("aka")
        addNew_user.save()
        
        # endi xuddi shu username li user qo'shishga urinib check qilamiz
        response = self.client.post(
            reverse("users:register"),
            data={
                "email": "aka1@gmail.com",
                "username": "aka",
                "first_name": "aka1",
                "last_name": "aka1",
                "password" : "something1",
            }
        )
        user_count_check = User.objects.count()

        self.assertEqual(user_count_check, 1)
        self.assertNotEqual(user_count_check, 0)
        self.assertFormError(response, "form", "username", "A user with that username already exists.")
         
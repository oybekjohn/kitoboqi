from urllib import response
from django.contrib.auth.models import User
from django.contrib.auth import get_user
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
         

class LoginTestCase(TestCase):
    def setUp(self):
        # DRY - Dont Repeat Yourself
        self.addNewtoDB_user = User.objects.create(username="aka", first_name="aka")
        self.addNewtoDB_user.set_password("aka")
        self.addNewtoDB_user.save()

        
    def test_successful_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "aka",
                "password": "aka",
            }
        )
        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)


    def test_wrong_credentials(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "wrong-username",
                "password": "aka",
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


        self.client.post(
            reverse("users:login"),
            data={
                "username": "aka",
                "password": "wrongpassword",
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


    def test_logout(self):
        self.client.login(username="usertes", password="testpass")

        self.client.get(reverse("users:logout"))

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)        



class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.url, reverse("users:login")+ "?next=/users/profile/")   # + loginrequiredmixin uchun
        self.assertEqual(response.status_code, 302)
    
    
    def test_profile_detail(self):
        test_user = User.objects.create(
            username="someone", first_name="something", last_name = "some", email="test@gmail.com"
            )
        test_user.set_password("root")
        test_user.save()

        self.client.login(username="someone", password="root")   #userni log in qildi, bundan pastida login holatda bo'ladi

        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_user.username)
        self.assertContains(response, test_user.first_name)
        self.assertContains(response, test_user.last_name)
        self.assertContains(response, test_user.email)
        
    
    def test_update_profile(self):
        # User modelga user(oybek) degan user yaratib olyabmiz
        user = User.objects.create(
            username="oybek", first_name="fname", last_name="lname", email="oybek@gmail.com"
        )
        user.set_password("root")
        user.save()
        self.client.login(username="oybek", password="root") # yaratilgan userni login qivolyabmiz

        # yaratilgan userni edit qilish uchun huddi UserUpdateForm kabi malumot uzatyabmiz
        response = self.client.post(
            reverse("users:profile-edit"),
            data={
                "username": "oybek",
                "first_name": "new_fname",
                "last_name": "lname",
                "email": "oybek@gmail.com"
            }
        )
        # va o'zgartiryotgan userni id si bilan ovolib refresh qilib qoyadi
        # user = User.objects.get(pk=user.pk)
        # yoki bu
        user.refresh_from_db()

        self.assertEqual(user.username, "oybek")
        self.assertEqual(user.first_name, "new_fname")
        self.assertEqual(response.url, reverse("users:profile"))


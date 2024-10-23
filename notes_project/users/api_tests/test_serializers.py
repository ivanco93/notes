from django.test import TestCase
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

class UserSerializerTests(TestCase):
    def test_user_register_serializer(self):
        # Verificar que el registro de un usuario funcione correctamente
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword'
        }
        serializer = UserRegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.username, data['username'])
        # Verificar que la contraseña se haya cifrado correctamente
        self.assertTrue(user.check_password(data['password']))

    def test_user_serializer(self):
        # Verificar la serialización de un usuario
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        serializer = UserSerializer(user)
        data = serializer.data
        self.assertEqual(data['id'], user.id)
        self.assertEqual(data['email'], user.email)
        self.assertEqual(data['username'], user.username)

    def test_user_update_serializer(self):
        # Verificar la actualización de un usuario
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            first_name='Old Name',
            last_name='Old Last Name',
            password='testpassword'
        )
        data = {
            'first_name': 'New Name',
            'last_name': 'New Last Name'
        }
        serializer = UserUpdateSerializer(user, data=data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        updated_user = serializer.save()
        self.assertEqual(updated_user.first_name, data['first_name'])
        self.assertEqual(updated_user.last_name, data['last_name'])

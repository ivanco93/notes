from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTestCase(TestCase):

    def test_create_user(self):
        # Prueba para crear un usuario
        user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.email, 'testuser@example.com')

    def test_user_authentication(self):
        # Prueba de autenticación con credenciales correctas
        user = User.objects.create_user(username='testuser', password='testpassword')
        authenticated_user = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(authenticated_user)

        # Prueba de autenticación con credenciales incorrectas
        wrong_credentials = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(wrong_credentials)

    def test_update_user(self):
        # Prueba para actualizar un usuario
        user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        user.username = 'newusername'
        user.email = 'newemail@example.com'
        user.save()

        updated_user = User.objects.get(id=user.id)
        self.assertEqual(updated_user.username, 'newusername')
        self.assertEqual(updated_user.email, 'newemail@example.com')

    def test_superuser(self):
        # Prueba para verificar un usuario con permisos de superusuario
        admin_user = User.objects.create_superuser(username='adminuser', password='adminpassword',
                                                   email='admin@example.com')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

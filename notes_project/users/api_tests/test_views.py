from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from notes.models import Note
from users.models import User

class NotesApiViewSetTestCase(APITestCase):
    def setUp(self):
        # Crear un usuario para autenticación
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.user_details_url = reverse('me')
        self.register_url = reverse('register_user')

        # Obtener el token de acceso
        login_url = reverse('token_obtain_pair')
        response = self.client.post(login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.access_token = response.data['access']

        # Configurar el cliente para usar el token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_register_user(self):
        # Probar que se puede registrar un nuevo usuario
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)  # Verificar que se ha creado un nuevo usuario

    def test_register_user_invalid_data(self):
        # Probar el registro con datos inválidos
        data = {
            'username': '',  # Nombre de usuario vacío
            'email': 'invalid-email',
            'password': 'short'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)  # No debería haber un nuevo usuario

    def test_get_user_details_authenticated(self):
        # Probar que un usuario autenticado puede obtener su información
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.user_details_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_update_user_details(self):
        # Probar que un usuario autenticado puede actualizar sus detalles
        self.client.login(username='testuser', password='testpassword')
        data = {
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.put(self.user_details_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')

    def test_update_user_details_unauthenticated(self):
        self.client.credentials()
        # Probar que un usuario no autenticado no puede actualizar sus detalles
        data = {
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.put(self.user_details_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_details_unauthenticated(self):
        self.client.credentials()
        # Probar que un usuario no autenticado no puede acceder a sus detalles
        response = self.client.get(self.user_details_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
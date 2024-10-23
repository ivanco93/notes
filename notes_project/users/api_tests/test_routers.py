from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from rest_framework import status
from users.api.views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class NotesRouterTestCase(APITestCase):
    def test_register_url_resolves(self):
        # Verificar que la URL para el registro de usuarios resuelve a la vista correcta
        url = reverse('register_user')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_login_url_resolves(self):
        # Verificar que la URL para la obtención del token resuelve a la vista correcta
        url = reverse('token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_refresh_url_resolves(self):
        # Verificar que la URL para refrescar el token resuelve a la vista correcta
        url = reverse('token_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_me_url_resolves(self):
        # Verificar que la URL para obtener los detalles del usuario resuelve a la vista correcta
        url = reverse('me')
        self.assertEqual(resolve(url).func.view_class, UserView)

    def test_register_user(self):
        # Probar que se puede registrar un nuevo usuario
        url = reverse('register_user')
        data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user(self):
        # Probar que un usuario puede obtener un token de acceso
        url = reverse('token_obtain_pair')
        # Primero registrar el usuario para autenticarlo después
        self.client.post(reverse('register_user'), {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        })
        # Intentar iniciar sesión
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_access_protected_route_without_token(self):
        # Probar que no se puede acceder a la ruta protegida sin un token
        url = reverse('me')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


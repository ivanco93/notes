from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from notes.models import Note
from users.models import User

class NotesApiViewSetTestCase(APITestCase):
    def setUp(self):
        # Crear un usuario para autenticación
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Obtener el token de acceso
        login_url = reverse('token_obtain_pair')
        response = self.client.post(login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.access_token = response.data['access']

        # Configurar el cliente para usar el token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        # Crear algunas notas para las pruebas
        self.note1 = Note.objects.create(
            title='Note One',
            description='Note one description',
            status=Note.Status.PENDIENTE
        )

        self.note2 = Note.objects.create(
            title='Note Two',
            description='Note two description',
            status=Note.Status.COMPLETADO
        )

    # Verificar que se puede obtener la lista de notas
    def test_list_notes(self):
        url = reverse('notes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Verificar que se puede crear una nueva nota
    def test_create_note(self):
        url = reverse('notes-list')
        data = {
            'title': 'New Note',
            'description': 'This is a new note',
            'status': Note.Status.PENDIENTE
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 3)

    # Verificar que se puede obtener una nota específica
    def test_retrieve_note(self):
        note_id = self.note1.id
        url = reverse('notes-detail', args=[note_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Note One')

    # Verificar que se puede actualizar una nota
    def test_update_note(self):
        note_id = self.note1.id
        url = reverse('notes-detail', args=[note_id])
        data = {
            'title': 'Updated Note',
            'description': 'Updated description',
            'status': Note.Status.COMPLETADO
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(id=note_id).title, 'Updated Note')

    # Verificar que se puede eliminar una nota
    def test_delete_note(self):
        note_id = self.note1.id
        url = reverse('notes-detail', args=[note_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 1)

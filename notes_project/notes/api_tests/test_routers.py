from django.urls import reverse, resolve
from django.test import SimpleTestCase
from notes.api.views import NotesApiViewSet
from notes.api.router import router_notes

class NotesRouterTestCase(SimpleTestCase):
    def setUp(self):
        self.router = router_notes

    def test_notes_url_patterns(self):
        # Verificar que la URL de la lista de notas esté resuelta correctamente
        url = reverse('notes-list')
        match = resolve(url)
        self.assertEqual(match.view_name, 'notes-list')

        # Verificar que la vista asignada a la URL es de tipo NotesApiViewSet
        self.assertTrue(hasattr(match.func, 'cls') and match.func.cls == NotesApiViewSet)

        # Verificar que la URL de detalle de notas esté resuelta correctamente
        note_id = 1
        url = reverse('notes-detail', args=[note_id])
        match = resolve(url)
        self.assertEqual(match.view_name, 'notes-detail')

        self.assertTrue(hasattr(match.func, 'cls') and match.func.cls == NotesApiViewSet)

    # Verificar que el enrutador tiene las vistas registradas
    def test_router_registers_correctly(self):
        url_names = [pattern.name for pattern in self.router.urls]
        self.assertIn('notes-list', url_names)
        self.assertIn('notes-detail', url_names)

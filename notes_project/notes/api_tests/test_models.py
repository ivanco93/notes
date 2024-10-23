from django.test import TestCase
from notes.models import Note
from django.utils import timezone

class NoteModelTestCase(TestCase):
    def setUp(self):
        Note.objects.create(
            id=1,
            title='Note One',
            description='Note one description',
            status=Note.Status.PENDIENTE
        )

        Note.objects.create(
            id=2,
            title='Note Two',
            description='Note two description',
            status=Note.Status.COMPLETADO
        )

        Note.objects.create(
            id=3,
            title="Note in PENDIENTE status",
            description="Note must be a PENDIENTE default status",
        )

    def test_assert_note(self):
        obj = Note.objects.get(id=2)
        self.assertEqual(obj.title, 'Note Two')
        self.assertEqual(obj.description, 'Note two description')
        self.assertEqual(obj.status, Note.Status.COMPLETADO)

    def test_unique_title(self):
        Note.objects.create(
            title="Unique note",
            description="First note with this title",
        )
        with self.assertRaises(Exception):
            Note.objects.create(
                title="Unique note",
                description="Second note with this title",
            )

    def test_default_status(self):
        obj = Note.objects.get(id=3)
        self.assertEqual(obj.status, Note.Status.PENDIENTE)


    def test_str_metodo(self):
        note = Note.objects.create(
            title="Test title",
            description="Test description",
        )
        self.assertEqual(str(note), "Test title")

    def test_created_at(self):
        note = Note.objects.create(
            title="Nota con fecha automática",
            description="Verificación de `created_at`.",
        )
        self.assertAlmostEqual(note.created_at, timezone.now(), delta=timezone.timedelta(seconds=1))
from rest_framework import serializers
from django.test import TestCase
from notes.models import Note
from notes.api.serializers import NoteSerializer

class NoteSerializerTestCase(TestCase):
    #inital setup
    def setUp(self):
        self.note = Note.objects.create(
            title='Test Note',
            description='Test description',
            status=Note.Status.PENDIENTE
        )
        self.serializer = NoteSerializer(instance=self.note)

    # Verify successfully fields serialization
    def test_note_serializer_fields(self):

        data = self.serializer.data
        self.assertEqual(data['id'], self.note.id)
        self.assertEqual(data['title'], self.note.title)
        self.assertEqual(data['description'], self.note.description)
        self.assertEqual(data['status'], self.note.status)

    # Test serializer validations with errors
    def test_note_serializer_validation(self):
        invalid_data = {
            'title': '',
            'description': 'Valid description',
            'status': Note.Status.PENDIENTE
        }
        serializer = NoteSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    # Test serializer validations with success
    def test_note_serializer_create(self):
        valid_data = {
            'title': 'New Note',
            'description': 'New note description',
            'status': Note.Status.COMPLETADO
        }
        serializer = NoteSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        note = serializer.save()
        self.assertEqual(note.title, valid_data['title'])
        self.assertEqual(note.description, valid_data['description'])
        self.assertEqual(note.status, valid_data['status'])

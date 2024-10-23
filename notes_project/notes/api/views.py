from rest_framework.viewsets import ModelViewSet

from notes.api.serializers import NoteSerializer
from notes.models import Note
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class NotesApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
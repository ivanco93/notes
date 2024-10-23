from rest_framework.routers import DefaultRouter
from notes.api.views import NotesApiViewSet

router_notes = DefaultRouter()
router_notes.register(prefix='notes', basename='notes', viewset=NotesApiViewSet)
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer, CollectionSubPreparer
from notes.models import Note
from django.contrib.auth import get_user_model

User = get_user_model()

nested_note_preparer = FieldsPreparer(fields={
    'url': 'get_absolute_url',
})


class NoteResource(DjangoResource):
    preparer = FieldsPreparer(
        fields={
            'id': 'id',
            'title': 'title',
            'text': 'text',
            'linked_notes': CollectionSubPreparer('linked_notes.all',
                                                  nested_note_preparer),
        })

    def is_authenticated(self):
        return self.request.user.is_authenticated()

    def list(self):
        return self.request.user.notes

    def detail(self, pk):
        return self.request.user.notes.get(pk=pk)

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
        if self.request.headers.get('Authorization') and self.request.headers[
                'Authorization'].startswith('Token'):
            _, token = self.request.headers['Authorization'].split(" ")
            try:
                user = User.objects.get(api_token=token)
                self.request.user = user
                return True
            except User.DoesNotExist:
                return False
        return False

    def list(self):
        return self.request.user.notes.all()

    def detail(self, pk):
        return self.request.user.notes.get(pk=pk)

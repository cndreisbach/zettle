from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

User = get_user_model()


class Note(models.Model):
    owner = models.ForeignKey(to=User,
                              on_delete=models.CASCADE,
                              related_name='notes')
    title = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(max_length=2000)
    linked_notes = models.ManyToManyField(to='self', symmetrical=True)

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})


class APIToken(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)

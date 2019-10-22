from django.db import models
from django.urls import reverse
from django.conf import settings
from hashids import Hashids
from django_extensions.db.models import TimeStampedModel

hashids = Hashids()


class Note(TimeStampedModel, models.Model):
    code = models.CharField(max_length=6, unique=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='notes')
    title = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(max_length=2000)
    linked_notes = models.ManyToManyField(to='self', symmetrical=True)

    def save(self, *args, **kwargs):
        """Add a unique short code to this note"""
        if not self.code:
            self.code = hashids.encode(self.owner.pk, self.pk)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})

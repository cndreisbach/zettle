from django.db import models
from django.urls import reverse
from django.conf import settings
import shortuuid
from django_extensions.db.models import TimeStampedModel

shortuuid.set_alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
CODE_LENGTH = 4


class Note(TimeStampedModel, models.Model):
    code = models.CharField(max_length=6, unique=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='notes')
    title = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(max_length=2000)
    linked_notes = models.ManyToManyField(to='self',
                                          symmetrical=True,
                                          blank=True)

    def set_code(self):
        code = None
        while code is None or Note.objects.filter(code=code).count():
            code = shortuuid.uuid()[:CODE_LENGTH]
        self.code = code

    def save(self, *args, **kwargs):
        """Add a unique short code to this note"""
        if not self.code:
            self.set_code()

        super().save(*args, **kwargs)

    def __str__(self):
        if self.code:
            return self.code

        if self.title:
            return self.title

        return self.text[:20] + "..."

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})

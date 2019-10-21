from django.db import models
from django.urls import reverse
from django.conf import settings


class Note(models.Model):
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='notes')
    title = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(max_length=2000)
    linked_notes = models.ManyToManyField(to='self', symmetrical=True)

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})

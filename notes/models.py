from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(to=User,
                              on_delete=models.CASCADE,
                              related_name='notes')
    title = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(max_length=2000)
    linked_notes = models.ManyToManyField(to='self', symmetrical=True)

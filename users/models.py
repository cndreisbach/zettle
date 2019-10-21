from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    api_token = models.UUIDField(default=uuid.uuid4, editable=False)

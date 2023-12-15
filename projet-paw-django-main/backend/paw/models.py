from django.db import models

from django.db import models
from django.utils import timezone
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=58)
    duration = models.PositiveIntegerField(help_text="Durée de la tache")
    comment = models.TextField(blank=True, null=True)
    state = models.BooleanField()
    
    def __str__(self):
        return f" task {self.user} N°{self.id}"

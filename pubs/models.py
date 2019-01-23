import uuid

from django.db import models

TYPE_CHOICES = (
    ('paper', 'Paper'),
    ('data', 'Data'),
)


class Publication(models.Model):
    title = models.CharField(max_length=1024)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField()
    description = models.TextField()
    url = models.URLField()
    approved = models.BooleanField(default=False)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

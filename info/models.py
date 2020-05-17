from django.db import models

# Create your models here.
class Graph(models.Model):
    """Model definition for Graph."""

    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)

    class Meta:
        """Meta definition for Graph."""

        verbose_name = 'Graph'
        verbose_name_plural = 'Graphs'
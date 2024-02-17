from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Título"
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    deadline = models.DateField(blank=False, null=False, verbose_name="Data de entrega")
    finished_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()

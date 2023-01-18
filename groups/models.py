from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'

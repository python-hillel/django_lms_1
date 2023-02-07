import datetime

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Group name: {self.name}'

    @classmethod
    def generate_fake_data(cls):
        for name in 'Python', 'Java', 'HTML+CSS', 'C#', 'C/C++', 'DevOPS':
            cls.objects.create(name=name)

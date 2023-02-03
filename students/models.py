import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

# from core.validators import validate_email_domain
from core.validators import ValidateEmailDomain
from groups.models import Group

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(models.Model):
    first_name_1 = models.CharField(max_length=50, verbose_name='First name', db_column='first',
                                    validators=[MinLengthValidator(3, message='"first_name" field value less then two symbols')])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last',
                                 validators=[MinLengthValidator(3)])
    # age = models.PositiveIntegerField()
    birthday = models.DateField(default=datetime.date.today, blank=True)       # default='2003-01-01'
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*VALID_DOMAINS)])
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    # email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name_1} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            s = cls()       # s = Student()
            s.first_name_1 = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name_1}.{s.last_name}@{f.random.choice(VALID_DOMAINS)}'           # name.last@domain
            s.birthday = f.date_between(start_date='-65y', end_date='-18y')
            # s.age = f.random_int(min=18, max=65)
            # f.random.choice()             DjDT
            s.save()


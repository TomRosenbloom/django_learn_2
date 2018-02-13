from django.db import models
from django.db.models import Model, CharField

from partial_date import PartialDateField

class Foo(Model):
    name = CharField(max_length=20,blank=True,null=True)
    date_of_birth = PartialDateField(blank=True, null=True)
    date_of_death = PartialDateField(blank=True, null=True)

    def __str__(self):
        return self.name

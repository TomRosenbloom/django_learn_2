from django.db.models import Model, CharField

from person.model_choices import *

class Person(Model):
    gender = CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.polynym_set.first().surname # rather than first, maybe set one of the roles as default
                                                # probably legal or preferred?

from django.db.models import Model, CharField, URLField, ImageField
from person_name.model_choices import *

# Create your models here.
class PersonNameStem(Model):
    role = CharField(
        max_length=20,
        choices=NAME_ROLES
    )

    class Meta:
       abstract = True


class Polynym(PersonNameStem):
    given = CharField(max_length=50, blank=True, null=True)
    middle = CharField(max_length=50, blank=True, null=True)
    moniker = CharField(max_length=50, blank=True, null=True)
    surname = CharField(max_length=50)
    generation = CharField(
        max_length=10,
        choices=GENERATION_CHOICES,
        blank=True
    )
    secondary_surname = CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return ('%s %s' % (self.given, self.surname))


class Mononym(PersonNameStem):
    mononym = CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.mononym


class Pictonym(PersonNameStem):
    url = URLField(blank=True, null=True)
    image = ImageField(blank=True, null=True)
    description = CharField(max_length=255)

    def __str__(self):
        return( 'Pictonym for person id %s' % (self.id))

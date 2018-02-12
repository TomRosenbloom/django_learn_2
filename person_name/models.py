from django.db import models
from person_name.model_choices import *

# Create your models here.
class PersonNameStem(models.Model):
    # type = models.CharField(
    #     max_length=20,
    #     choices=NAME_TYPES,
    #     blank=True
    # )
    # hmmm, there's going to be a lot of redundant fields for some name types...
    # perhaps as ther are only three types I should have a class for each of these
    # polynym is what will be used in nearly all cases
    role = models.CharField(
        max_length=20,
        choices=NAME_ROLES,
        blank=True
    )

   class Meta:
       abstract = True


class Polynym(PersonNameStem):
    given = models.CharField(max_length=50, blank=True, null=True)
    middle = models.CharField(max_length=50, blank=True, null=True)
    moniker = models.Charfield(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    generation = models.CharField(
        max_length=10,
        choices=GENERATION_CHOICES,
        blank=True
    )
    secondary_surname = models.CharField(max_length=50, blank=True, null=True)

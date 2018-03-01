from django.db.models import Model, CharField, DateField, PositiveIntegerField
from datetime import date, datetime
from django.core.validators import MaxValueValidator, MinValueValidator

#from partial_date import PartialDateField

from person.model_choices import *

class Person(Model):
    gender = CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )
    birth_year = PositiveIntegerField(
        validators=[
            MinValueValidator(0000),
            MaxValueValidator(datetime.now().year)
            ],
        blank = True,
        null = True
    )
    birth_month = PositiveIntegerField(
        choices = MONTH_CHOICES,
        blank = True,
        null = True
    )
    birth_monthday = PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(31)
            ],
        blank = True,
        null = True
    )
    date_of_birth = DateField(
        help_text = "A date wil be created if the following are set: just a year; a year and a month; a year, a month and a day number",
        blank = True,
        null = True
    )

    def save(self, *args, **kwargs):
        # if we have just a year, a year and a month, or all three date elements, then we can construct and save a date
        if self.birth_year is not None and self.birth_month is not None and self.birth_monthday is not None:
            # all three date elements are set
            self.date_of_birth = date(self.birth_year, self.birth_month, self.birth_monthday)
        elif self.birth_year is not None and self.birth_month is not None:
            # the year and the month are set (but by implication of being here not the day)
            self.date_of_birth = date(self.birth_year, self.birth_month, 1)
        elif self.birth_year is not None and self.birth_month is None and self.birth_monthday is None:
            # only the year is set
            self.date_of_birth = date(self.birth_year, 1, 1)
        else:
            # any other combination
            self.date_of_birth = None
        super(Person, self).save(*args, **kwargs)


    def __str__(self):
        return self.polynym_set.first().surname # rather than first, maybe set one of the roles as default
                                                # probably legal or preferred?
        #return self.id # temporary - the above causes an error if no polynym exists, obvs

from django.db.models import Model, CharField, DateField
from datetime import date

#from partial_date import PartialDateField

from person.model_choices import *

class Person(Model):
    PARTIAL_YEAR='%Y'
    PARTIAL_MONTH='%Y-%m'
    PARTIAL_DAY='%Y-%m-%d'
    PARTIAL_DATE_CHOICES = (
        (PARTIAL_YEAR, 'Year'),
        (PARTIAL_MONTH, 'Month'),
        (PARTIAL_DAY, 'Day'),
    )
    gender = CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )
    partial_date = CharField( # https://stackoverflow.com/questions/30134526/date-conveniences-validation-display-etc-for-partial-dates-in-django
        choices = PARTIAL_DATE_CHOICES,
        max_length=10,
        blank = True,
        null = True
    )
    date_of_birth = DateField(blank = True, null = True)
    # date_of_birth = PartialDateField(blank=True, null=True)
    # date_of_death = PartialDateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.partial_date == self.PARTIAL_YEAR:
            self.date_of_birth = date(self.date_of_birth.year, 1, 1)
        elif self.partial_date == self.PARTIAL_MONTH:
            self.date_of_birth = date(self.date_of_birth.year, self.date_of_birth.month, 1)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.polynym_set.first().surname # rather than first, maybe set one of the roles as default
                                                # probably legal or preferred?
        #return self.id # temporary - the above causes an error if a name is not entered, obvs
        #...which I discovered when testing the partial dates thing
        # just for now have to *remember to* enter at least one name
        # Have to remember this is admin interface...
        # in public interface would need to enforce this
        #  - except in this instance I don't want to make an external admin user, that's kind of the point

        # On the front you could present this in different ways, e.g. three drop downs
        # for year/month/date (including 'none selected') then process them appropriately after form submission
        # The important thing here is getting the data model right, i.e. avoiding use of any text fields
        # to store dates e.g. if only the year is known
        # For year, if there is a large range, a validated text input may be best

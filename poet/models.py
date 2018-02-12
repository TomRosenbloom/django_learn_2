from django.db import models

# Create your models here.
class Poet(models.Model):
    """
    should I create an app for 'name' (much as I might for 'address')
    then any object that is a type of person and has a name will have a one-to-one rel
    see this https://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields
    about names...
    ...and google something like 'database modelling person names' and down a rabbit hole we go...
    I think the problem is how a system like Django deals with such a rel
    i.e. interms of creating forms and what have you
    like, it should be model Poet extends Person has link(s) to Name(s)
    How do we deal with the fact that a person can have more than one type of name
    with different roles - see the SO link above?
    In that case the only common fields are type (Polynym, Mononym, Pictonym) and
    role (legal, marital, maiden, preferred, sobriquet, pseudonym...)
    - what about the fact that, as in the SO example, multiple name roles may duplicate
    fields e.g. Malcolm X has the same given name for his preferred and legal names,
    (whereas the 'given' of his legal name is different ie Malik)
    """
    surname = models.CharField(max_length=50, blank=True, null=True)
    forename = models.Charfield(max_length=50, blank=True, null=True)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    pseudonym = models.CharField(max_length=50, blank=True, null=True)
    pref_name = models.CharField(max_length=50, blank=True, null=True)

    funders = models.ManyToManyField(Funder)
    project_name = models.CharField(max_length=255,unique=True)
    stage = models.CharField(
        max_length=4,
        choices=STAGE_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.project_name

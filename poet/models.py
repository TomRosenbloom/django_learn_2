from django.db.models import Model, ForeignKey
from person_name.models import Polynym, Mononym, Pictonym

class Poet(Model):
    polynyms = ForeignKey(Polynym)
    mononyms = ForeignKey(Mononym)
    pictonyms = ForeignKey(Pictonym)

    def __str__(self):
        return self.polynyms_set.first().surname

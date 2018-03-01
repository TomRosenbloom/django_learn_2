from django.db.models import Model, CharField

from person.models import Person


class Poet(Person):
    token = CharField(max_length=50, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Poet, self).__init__(*args, **kwargs)
        self.__name_count__ = None

    def clean(self):
        if self.token is None:
            self.token = '%s %s' % (self.polynym_set.first().given, self.polynym_set.first().surname)
        # print(self.__name_count__) # none

    # def save(self):
    #     print(self.__name_count__) # 1 (or whatever)

    def __str__(self):
        #return self.polynym_set.first().surname # rather than first, maybe set one of the roles as default
                                                # probably legal or preferred?
        return ('%s %s' % (self.polynym_set.first().given, self.polynym_set.first().surname))

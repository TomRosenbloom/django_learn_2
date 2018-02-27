from django.contrib import admin

from person.models import Person
from person_name.models import Polynym, Mononym, Pictonym
from poet.models import Poet

class PolynymInline(admin.StackedInline):
    model = Polynym
    extra = 0

class MononymInline(admin.TabularInline):
    model = Mononym
    extra = 0

class PictonymInline(admin.TabularInline):
    model = Pictonym
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PolynymInline,
        MononymInline,
        PictonymInline
    ]

class PoetAdmin(admin.ModelAdmin):
    inlines = [
        PolynymInline,
        MononymInline,
        PictonymInline
    ]
    readonly_fields = ('date_of_birth',)
    fields = ('token', 'gender', 'birth_year', 'birth_month', 'birth_monthday', 'date_of_birth')

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Polynym)
admin.site.register(Mononym)
admin.site.register(Pictonym)
admin.site.register(Poet, PoetAdmin)

# so... can I add an overiding class in here that will sort out admin
# for Poet? That is, whereas currently we just see three drop downs for the foreign
# key rels to Polynymic etc., have those expanded out so to speak, so we can
# enter a polynymic (or two) for the poet in the Poet admin screen?
# Sounds a tall order, but...

# class PolynymInline(admin.TabularInline):
#     model = Polynym
#
# class MononymInline(admin.TabularInline):
#     model = Mononym
#
# class PoetAdmin(admin.ModelAdmin):
#     inlines = [
#         PolynymInline,
#         MononymInline
#     ]

# this works perfectly, but does show up a problem in my models, I think
# if you choose to add a polynym, you have the a choice of 'role': legal, preferred, pseudonym etc.
# but these all have the same fields (of course) and some (1) don't really fit (2) would be duplicates
# e.g. the difference between preferred (or legal, maybe) and maiden name might just be one field the surname
# e.g. ah wait - more subtle: soubriquet is appearing in the roles list for polynyms
# when soubriquet is by definition a mononym...
# hmmm... in https://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields
# roles are not limitted to certain types of name e.g. for Prince, he has a polynym with
# a role of legal, but his pictonym also has that role...
# But, when for e.g. we select to add a Polynym, we don't want soubriquet in the list
# and when for e.g. we choose to add a mononym, we don't want er... or do we??
# need to think on this...
# ...actually I think it's fine
# However, I have done the foreign key rels for poet and polynym etc the wrong way round
# (and should I make a person model and have poet extend that??)

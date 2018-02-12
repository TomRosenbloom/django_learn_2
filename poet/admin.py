from django.contrib import admin

from poet.models import Poet
from person_name.models import Polynym

# Register your models here.
admin.site.register(Poet)
admin.site.register(Polynym)

# so... can I add an overiding class in here that will sort out admin
# for Poet? That is, whereas currently we just see three drop downs for the foreign
# key rels to Polynymic etc., have those expanded out so to speak, so we can
# enter a polynymic (or two) for the poet in the Poet admin screen?
# Sounds a tall order, but...

class PolynymInline(admin.TabularInline):
    model = Polynym

class PoetAdmin(admin.ModelAdmin):
    inlines = [
        PolynymInline,
    ]

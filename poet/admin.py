from django.contrib import admin

from django.forms.models import BaseInlineFormSet
from django import forms

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

class PoetAdminForm(forms.ModelForm):
    def clean(self):
        if self.data["polynym_set-TOTAL_FORMS"] == '0' and self.data["mononym_set-TOTAL_FORMS"] == '0' and self.data["pictonym_set-TOTAL_FORMS"] == '0':
            raise forms.ValidationError("At least one name must be entered")

class PoetAdmin(admin.ModelAdmin):
    inlines = [
        PolynymInline,
        MononymInline,
        PictonymInline
    ]
    readonly_fields = ('date_of_birth',)
    fields = ('token', 'gender', 'birth_year', 'birth_month', 'birth_monthday', 'date_of_birth')
    form = PoetAdminForm


# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Polynym)
admin.site.register(Mononym)
admin.site.register(Pictonym)
admin.site.register(Poet, PoetAdmin)

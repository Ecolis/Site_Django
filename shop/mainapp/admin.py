from django.contrib import admin
from django import forms
from django.forms import ModelChoiceField

from .models import *


class DressAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects. filter(slug='Dress'))
            return super().formfield_for_foreingkey(db_field, request, **kwargs)


class skirtAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects. filter(slug='skirt'))
            return super().formfield_for_foreingkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Dress, DressAdmin)
admin.site.register(skirt, skirtAdmin)
admin.site.register(Cart)
admin.site.register(Customer)

from django.contrib import admin
from .models import Collaborator, SupportingMaterial, Article


class SupportingInline(admin.StackedInline):
    model = SupportingMaterial


class CollaboratorInline(admin.StackedInline):
    model = Collaborator


class CompanionArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'doi', 'abstract_text', 'document', 'modified')
    date_heirarchy = ['created']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SupportingInline]


class CollaboratorAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']


class SupportingMaterialAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']


admin.site.register(Article, CompanionArticleAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(SupportingMaterial, SupportingMaterialAdmin)

from django.contrib import admin

from .models import Reaction


class ReactionAdmin(admin.ModelAdmin):
    list_display = ('reaction_type',)


admin.site.register(Reaction, ReactionAdmin)

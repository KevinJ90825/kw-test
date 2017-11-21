from django.contrib import admin

from main.models import HomeBuyer


class HomeBuyerAdmin(admin.ModelAdmin):
    model = HomeBuyer
    exclude = ()
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(HomeBuyer, HomeBuyerAdmin)


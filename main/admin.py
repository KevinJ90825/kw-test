from django.contrib import admin

from main.models import HomeBuyer


class HomeBuyerAdmin(admin.ModelAdmin):
    model = HomeBuyer
    exclude = ()


admin.site.register(HomeBuyer, HomeBuyerAdmin)


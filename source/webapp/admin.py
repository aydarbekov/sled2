from django.contrib import admin

from webapp.models import Firma, Supliers, People, OpenBudget, Tender, Lot

admin.site.register(Firma)
admin.site.register(Supliers)
admin.site.register(People)
admin.site.register(OpenBudget)
admin.site.register(Tender)
admin.site.register(Lot)
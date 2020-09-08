from django.contrib import admin
from .models import canditates,rounds_table,role_table
admin.site.register(canditates)
admin.site.register(role_table)
admin.site.register(rounds_table)
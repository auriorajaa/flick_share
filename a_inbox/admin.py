from django.contrib import admin
from .models import *

# Register your models here.

class InboxMessageAdmin(admin.ModelAdmin):
  readonly_fields = ('sender', 'conversation', 'body')

admin.site.register(InboxMessage, InboxMessageAdmin)
admin.site.register(Conversation)
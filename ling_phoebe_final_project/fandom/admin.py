from django.contrib import admin

from .models import Company, Group, Style, Entertainer, EntertainerGroup, Album, Song, Role, Create, EventCategory, \
    Event, Activity

admin.site.register(Company)
admin.site.register(Group)
admin.site.register(Style)
admin.site.register(Entertainer)
admin.site.register(EntertainerGroup)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Role)
admin.site.register(Create)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Activity)

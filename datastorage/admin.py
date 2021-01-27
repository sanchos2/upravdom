from django.contrib import admin

from datastorage.models import IMD, Entrance, House, IMDValue, Placement


class HouseAdmin(admin.ModelAdmin):  # noqa: D101

    list_display = ['title', 'energy_efficiency']


class EntranceAdmin(admin.ModelAdmin):  # noqa: D101

    list_display = ['house', 'number', 'placement_on_level', 'total_level']


class IMDInline(admin.TabularInline):  # noqa: D101
    model = IMD
    extra = 0


class IMDValueInline(admin.TabularInline):  # noqa: D101
    model = IMDValue
    extra = 0


class PlacementAdmin(admin.ModelAdmin):  # noqa: D101

    list_display = ['number', 'placement_type', 'total_space', 'living_space', 'entrance', 'level', 'position']
    search_fields = ['number']
    inlines = [IMDInline]


class IMDAdmin(admin.ModelAdmin):  # noqa: D101

    list_display = ['placement', 'title', 'imd_number', 'initial_value', 'created_at', 'is_active']
    list_editable = ['is_active']
    inlines = [IMDValueInline]


admin.site.register(House, HouseAdmin)
admin.site.register(Entrance, EntranceAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(IMD, IMDAdmin)

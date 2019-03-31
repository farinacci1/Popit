from django.contrib import admin
from django.contrib.auth import get_user_model

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Profile
admin.site.site_header = ' POPIT Administration'

class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    inlines = [ UserProfileInline,]
    list_display = ('email', 'admin','staff','active','confirmed')
    list_filter = ('admin','staff','active','confirmed')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('User info', {'fields': ('first_name','last_name','confirmed')}),
        ('Permissions', {'fields': ('admin','staff',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

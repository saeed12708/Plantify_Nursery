from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Blog, Location, Offer, Cart, Favorite, Notification, Order,PaymentMethod,UserProfile,HomeBanner

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(User, UserAdmin)

# Registering models
admin.site.register(Blog)
admin.site.register(Location)
admin.site.register(Offer)
admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(Notification)
admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(UserProfile)
admin.site.register(HomeBanner)


# Register your models here.

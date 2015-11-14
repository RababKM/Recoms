from django.contrib import admin
from main.models import Recommendation, Category

# Register your models here.


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Category, CategoryAdmin)

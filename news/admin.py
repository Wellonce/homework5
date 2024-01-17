from django.contrib import admin
from .models import New, Comment, Tag, New_tag

# Register your models here.
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(New_tag)
class New_tagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
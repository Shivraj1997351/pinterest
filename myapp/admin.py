from django.contrib import admin
from myapp.models import Post
# Register your models here.
@admin.register(Post)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id','user','photo','date']




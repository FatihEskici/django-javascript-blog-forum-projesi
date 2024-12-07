from django.contrib import admin
from django.templatetags.static import static
from .models import Post, Comment, Category


admin.site.site_header = "Yönetim Paneli"
admin.site.site_title = "Yönetim Paneli"
admin.site.index_title = "Yönetim Paneline Hoşgeldiniz"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    search_fields = ('title', 'content')  
    list_filter = ('created_at', 'category', 'is_published')  
    ordering = ('-created_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_at', 'approved')  
    search_fields = ('name', 'email', 'body')  
    list_filter = ('created_at', 'approved')  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)

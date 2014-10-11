from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post,Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()
        widgets = {
            'content' : CKEditorWidget(),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content',)
    list_filter = ('categories',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)

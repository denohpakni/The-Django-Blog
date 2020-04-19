from django.contrib import admin
from my_blog.models import Post

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


# we can customize the way data is displayed in the administration panel according to our convenience.
# This will make our admin dashboard more efficient. 
# You will see more details about the Post.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content'] # a search bar at the top of the list, which will search the database from the search_fields attributes.
    prepopulated_fields = {'slug':('title',)} # populates the slug, now if you create a post the slug will automatically be filled based upon your title.

admin.site.register(Post, PostAdmin)
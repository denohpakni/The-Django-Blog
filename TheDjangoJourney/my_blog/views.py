#
from django.shortcuts import render
#
from django.views import generic
# import the Posts
from my_blog.models import Post

# Create your views here.
# We’re going to use class-based views then map URLs for each view 
# and create an HTML templated for the data returned from the views.
class PostList(generic.ListView):
    # The built-in ListViews which is a subclass of generic class-based-views render a list with the objects of the specified model we just need to mention the template
    # we have applied a filter so that only the post with status published be shown at the front end of our blog.
    # Also in the same query, we have arranged all the posts by their creation date. The ( – ) sign before the created_on signifies the latest post would be at the top and so on.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    #  DetailView provides a detailed view for a given object of the model at the provided template.
    model = Post
    template_name = 'post_detail.html'
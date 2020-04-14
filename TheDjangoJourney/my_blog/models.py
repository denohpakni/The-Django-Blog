#  importing the class models
from django.db import models
# creating a subclass of models.Model
from django.contrib.auth.models import User

# Create your models here.

# we declared a tuple for STATUS of a post to keep draft and published posts separated when we render them out with templates.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    upldated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    """ # The Meta class inside the model contains metadata.
    We tell Django to sort results in the created_on field in descending order by default when we query the database. 
    We specify descending order using the negative prefix. 
    By doing so, posts published recently will appear first."""
    class Meta:
        ordering = ['-created_on']

    # The __str__() method is the default human-readable representation of the object.
    # Django will use it in many places, such as the administration site.
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Link(models.Model):
    """
    Title returns the name of the website
    site_url provides link to the site
    Content returns decription of the website
    """
    title= models.CharField(max_length=200)
    site_url= models.URLField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title


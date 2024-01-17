from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)


class Category(AbstractBaseModel):
    name= models.CharField(max_length= 128,)

class New(AbstractBaseModel):
    title = models.CharField(max_length= 128)
    body = models.TextField()
    img = models.ImageField(upload_to= "news/")

    def __str__(self):
        return self.title

class Tag(AbstractBaseModel):
    text = models.TextField()


class New_tag(AbstractBaseModel):
    tag_id= models.ForeignKey(Tag, on_delete= models.CASCADE)
    news_id = models.ForeignKey(New, on_delete= models.CASCADE)



class Comment(AbstractBaseModel):
    body = models.TextField()
    author_id= models.ForeignKey(User, on_delete= models.CASCADE)
    news_id= models.ForeignKey(New, on_delete= models.CASCADE)

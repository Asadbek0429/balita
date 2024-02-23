from django.db import models
from config.base_model import BaseModel
from ckeditor.fields import RichTextField


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post')
    description = RichTextField()
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

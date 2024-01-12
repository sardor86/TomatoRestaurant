from django.db import models

from shop.models import User


class Blog(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=50)
    short_description = models.TextField(max_length=500)
    description = models.TextField(max_length=1500)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self) -> str:
        return f'Blog<{self.title}>'

    def __repr__(self) -> str:
        return f'Blog<{self.title}>'


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)

    class Meta:
        db_table = 'blog_comment'
        verbose_name = 'comment'
        verbose_name_plural = 'blog comments'

    def __str__(self) -> str:
        return f'BlogComment<{self.comment}>'

    def __repr__(self) -> str:
        return f'Comment<{self.comment}>'

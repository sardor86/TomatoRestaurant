from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)

    class Meta:
        db_table = 'blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self) -> str:
        return f'Blog<{self.title}>'

    def __repr__(self) -> str:
        return f'Blog<{self.title}>'

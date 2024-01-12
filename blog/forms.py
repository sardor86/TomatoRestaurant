from django import forms

from .models import BlogComment


class BlogCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(), max_length=400)

    def save(self, blog_id, user_id):
        comment = BlogComment.objects.filter(blog_id=blog_id, user_id=user_id).first()

        if comment:
            comment.comment = self.cleaned_data['comment']
            comment.save()
            return True

        BlogComment(blog_id=blog_id,
                    user_id=user_id,
                    comment=self.cleaned_data['comment']).save()

from django import forms

from shop.models import Rating


class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.HiddenInput(), max_value=5, min_value=1)
    comment = forms.CharField(widget=forms.Textarea(), max_length=400)

    def save(self, meal_id, user_id):
        rating = Rating.objects.filter(meal_id=meal_id, user_id=user_id).first()

        if rating:
            rating.rating = self.cleaned_data['rating']
            rating.comment = self.cleaned_data['comment']
            rating.save()
            return True

        Rating(meal_id=meal_id,
               user_id=user_id,
               rating=self.cleaned_data['rating'],
               comment=self.cleaned_data['comment']).save()

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from catalog.models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", "email", )


class NewsForm(forms.ModelForm):
    redactor = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all(),
                                              widget=forms.CheckboxSelectMultiple,
                                              required=False
                                              )

    class Meta:
        model = Newspaper
        fields = ('title', 'content', 'published_date', 'topics')


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False,
                            label="", widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}))


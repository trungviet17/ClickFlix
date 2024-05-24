from django import forms
from main.models import Category


class MovieFilterForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, label="Title")
    # score_min = forms.FloatField(required=False, label="Min Score")
    # score_max = forms.FloatField(required=False, label="Max Score")
    # popularity_min = forms.FloatField(required=False, label="Min Popularity")
    # popularity_max = forms.FloatField(required=False, label="Max Popularity")
    price_min = forms.DecimalField(
        max_digits=10, decimal_places=2, required=False, label="Min Price"
    )
    price_max = forms.DecimalField(
        max_digits=10, decimal_places=2, required=False, label="Max Price"
    )
    # language = forms.CharField(max_length=5, required=False, label="Language")
    # released_after = forms.DateField(
    #     required=False,
    #     widget=forms.DateInput(attrs={"type": "date"}),
    #     label="Released After",
    # )
    # released_before = forms.DateField(
    #     required=False,
    #     widget=forms.DateInput(attrs={"type": "date"}),
    #     label="Released Before",
    # )
    # keyword = forms.CharField(max_length=200, required=False, label="Keyword")
    # actors = forms.ModelMultipleChoiceField(
    #     queryset=Actor.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     label="Actors",
    # )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Categories",
    )


class RechargeForm(forms.Form):
    code = forms.CharField(label="Recharge Code", max_length=50)

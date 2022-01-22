from django import forms
from .models import News
from django.conf import settings
	


class NewsAddForm(forms.ModelForm):
	
	created_at = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={"placeholder":"ДД.ММ.ГГГГ"}))
	class Meta:
		model = News
		fields = (
			'title',
			'content',
			'created_at'
		)

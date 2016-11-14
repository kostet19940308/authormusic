# coding: utf-8

from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, label=u'Поиск по альбомам', required=False)
    sort = forms.TypedChoiceField(empty_value='-created_in', required=False,
                                  choices=[('-created_in', u'По убыванию'), ('created_in', u'По возрастанию')],
                                  label=u'Сортировать по')
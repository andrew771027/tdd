from django import forms
from lists.models import Item, List
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

EMPTY_ITEM_ERROR = "You can't have an empty list item."
DUPLICATE_ITEM_ERROR = "You've already got this in your list."


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={'placeholder': 'Enter a to-do item',
                                                  'class': 'form-control input-lg',
                                                  },


                                           ),
        }
        error_messages = {
            'text': {
                'invalid': "Enter an invalid item",
                'required': _(EMPTY_ITEM_ERROR)
            },
        }


class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self) -> None:
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)


class NewListForm(ItemForm):

    def save(self, owner):
        if owner.is_authenticated():
            List.create_new(
                first_itm_text=self.cleaned_data['text'], owner=owner)
        else:
            List.create_new(first_item_text=self.cleaned_data['text'])

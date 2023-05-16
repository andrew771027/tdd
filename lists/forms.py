from django import forms
from lists.models import Item
from django.utils.translation import gettext_lazy as _

EMPTY_ITEM_ERROR = "You can't have an empty list item."

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

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()
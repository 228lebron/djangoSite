from django.forms import ModelForm, DecimalField
from .models import Quote
class BbForm(ModelForm):
    class Meta:
        model = Quote
        fields = ('part_number', 'brand', 'compel_price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['part_number'].label = 'Номер детали'
        self.fields['brand'].label = 'Бренд'
        self.fields['compel_price'].label = 'Цена'

from django import forms
from cars.models import Brand

class CarForm(forms.Form):

    model = forms.CharField(max_length=200)

    #na hora que o usuario for preencher esse input vai acontecer o seguinte, vai ser realizado uma query no banco de dados, já que esse método retorna uma queryset do BD com todas as Brands(Marcas)
    Brand = forms.ModelChoiceField(Brand.objects.all())
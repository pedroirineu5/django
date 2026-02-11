from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):

#     model = forms.CharField(max_length=200)

#     #na hora que o usuario for preencher esse input vai acontecer o seguinte, vai ser realizado uma query no banco de dados, já que esse método retorna uma queryset do BD com todas as Brands(Marcas)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.IntegerField()
#     photo = forms.ImageField()

#     def save(self):

#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

from django.db import models

class Brand(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Car vai ser o nome da tabela no banco de dados
class Car(models.Model):

    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    #                                   v   impede que a tentativa de deleção da brand apague todos os carros, logo para deletar a brand precisa deletar todos os carros.
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value= models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    
    # subscrevendo a função padrão, de criar retornar object 1,2.... para o nome do modelo mesmo.
    # Tipo toString() do java
    def __str__(self):
        return self.model
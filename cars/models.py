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
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_name')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value= models.FloatField(blank=True, null=True)
    
    # subscrevendo a função padrão, de criar retornar object 1,2.... para o nome do modelo mesmo.
    # Tipo toString() do java
    def __str__(self):
        return self.model
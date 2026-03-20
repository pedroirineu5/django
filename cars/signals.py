from django.db.models.signals import pre_save, pre_delete, post_delete, post_init, post_save
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')


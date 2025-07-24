from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Donation, Receive, Stock

#increase the stock on donation
@receiver(post_save,sender=Donation)
def update_stock_on_donation(sender, instance, created, **kwargs):
    if created:
        blood_group = instance.p_id.p_blood_grp
        quantity = instance.quantity

        stock, _ = Stock.objects.get_or_create(s_blood_group = blood_group)
        stock.quantity += quantity
        stock.save()

#decrease the stock on receive
@receiver(post_save,sender=Receive)
def update_stock_on_receive(sender, instance, created, **kwargs):
    if created:
        blood_group = instance.r_blood_group
        quantity = instance.quantity

        try:
            stock = Stock.objects.get(s_blood_group = blood_group)
            if stock.quantity >= quantity:
                stock.quantity -= quantity
                stock.save()
            else:
                print(f"Not enough stock for {blood_group}")

        except stock.DoesNotExist:
            print(f"No stock entry for {blood_group}")
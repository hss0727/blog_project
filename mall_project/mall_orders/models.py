from django.db import models


class MallOrderClass(models.Model):

    ordering_user = models.ForeignKey(
        "mall_users.MallUserClass", 
        on_delete=models.CASCADE, 
        verbose_name="Ordering User"
    )

    ordering_product = models.ForeignKey(
        "mall_products.MallProductClass",
        on_delete=models.CASCADE,
        verbose_name="Ordering Product",
    )

    ordering_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Ordering Date Time",
    )

    ordering_quantity = models.IntegerField(
        verbose_name="Ordering Quantity",
    )

    def __str__(self):
        return str(self.ordering_user) + str(self.ordering_product)

    class Meta:
        db_table = "mall_order_db"
        verbose_name = "Orders"
        verbose_name_plural = "Orders"
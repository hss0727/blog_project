from django.db import models


class MallProductClass(models.Model):
    product_name = models.CharField(
        max_length=256,
        verbose_name="Product Name",
    )

    product_price = models.IntegerField(
        verbose_name="Product Price",
    )

    product_description = models.TextField(
        verbose_name="Product Description",
    )

    product_stock = models.IntegerField(
        verbose_name="Product Stock",
    )

    product_reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Registered Date Time of the Product",
    )

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "mall_product_db"
        verbose_name = "Products"
        verbose_name_plural = "Products"
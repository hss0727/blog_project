from django.db import models


class MallUserClass(models.Model):
    user_email = models.EmailField(
        verbose_name="User Email",
    )

    user_pw = models.CharField(
        max_length=64,
        verbose_name="User Password",
    )

    registered_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Registered Date Time",
    )

    def __str__(self):
        return self.user_email

    class Meta:
        db_table = "mall_users_db"
        verbose_name = "Mall Users"
        verbose_name_plural = "Mall Users"


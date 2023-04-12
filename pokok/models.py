from django.db import models

# Create your models here.


class pokok(models.Model):
    pokok_id = models.PositiveBigIntegerField()
    pokok_name = models.CharField(max_length=100)
    grow_date = models.DateField()
    height_date = models.FloatField()
    leaf_colour = models.CharField(max_length=50)

    def __str__(self) -> str:
        # return super().__str__()
        return f'{self.pokok_name} {self.pokok_id}'

from django.db import models
from django.db.models import QuerySet

from abstracts.models import (
    AbstractModel,
    AbstractManager,
    AbstractQuerySet
)


# Create your models here.
class Pen(AbstractModel):
    """Main class for pen"""

    STATUS_PATTERN = [
        ('Red', 'Красная'),
        ('Black', 'Черная'),
        ('Green', 'Зеленая'),
        ('Violet', 'Фиолетовая')
    ]

    title = models.CharField(
        verbose_name="название",
        max_length=200
    )

    form = models.CharField(
        verbose_name="форма",
        max_length=200
    )

    color = models.CharField(
        max_length=80,
        verbose_name="цвет",
        choices=STATUS_PATTERN,
        default='Unkown_type'
    )

    class Meta:
        ordering = (
            "-color",
        )
        verbose_name = "ручка"
        verbose_name_plural = "ручки"

    def __str__(self) -> str:
        return f'Pen name - {self.title}| Form -  {self.form} | Color - {self.color}'


class Quantity(models.Model):
    """Main class for quantity of pen"""

    number = models.OneToOneField(
        Pen,
        on_delete=models.CASCADE,
        verbose_name='ручка'
    )

    quantity_of_pen = models.IntegerField(
        verbose_name='количество'
    )

    class Meta:
        ordering = (
            'number',
        )
        verbose_name = 'штука'
        verbose_name_plural = 'штуки'

    def __str__(self) -> str:
        return f'{self.number}'

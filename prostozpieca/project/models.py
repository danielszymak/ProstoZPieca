from django.db import models


# Create your models here.

class Bakings(models.Model):
    name = models.CharField("Name of baking", unique=True, max_length=128)
    perform_count = models.PositiveIntegerField("Total count of realizations of this recipe", default=0, blank=True)
    grade = models.DecimalField("Average grade of recipe", decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return self.name


class ProportionBaking(models.Model):

    baking = models.ForeignKey(Bakings, on_delete=models.CASCADE, verbose_name="Name of baking")
    water_to_flour = models.DecimalField("Water to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    milk_to_flour = models.DecimalField("Milk to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    salt_to_flour = models.DecimalField("Salt to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    oil_to_flour = models.DecimalField("Oil to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    butter_to_flour = models.DecimalField("Butter to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    sourdough_to_flour = models.DecimalField("Sourdough to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    poolish_to_flour = models.DecimalField("Poolish to flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    wheat550_to_whole = models.DecimalField("550 type wheat flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    wheat00_to_whole = models.DecimalField("00 type wheat flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    wheat650_to_whole = models.DecimalField("650 type wheat flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    wheat2000_to_whole = models.DecimalField("2000 type wheat flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    rye720_to_whole = models.DecimalField("720 type rye flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    rye2000_to_whole = models.DecimalField("2000 type rye flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)
    spelt650_to_whole = models.DecimalField("650 type rye flour to whole flour ratio in recipe", decimal_places=3, max_digits=10, default=0.00)

    def __str__(self):
        return self.baking

    class Meta:

        constraints = [models.CheckConstraint(check=models.Q(water_to_flour__gte=0),
                                              name='Water to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(milk_to_flour__gte=0),
                                              name='Milk to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(salt_to_flour__gte=0),
                                              name='Salt to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(oil_to_flour__gte=0),
                                              name='Oil to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(butter_to_flour__gte=0),
                                              name='Butter to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(sourdough_to_flour__gte=0),
                                              name='Sourdough to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(poolish_to_flour__gte=0),
                                              name='Poolish to flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(wheat550_to_whole__gte=0),
                                              name='550 type wheat flour to whole flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(wheat00_to_whole__gte=0),
                                              name='00 type wheat flour to whole flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(wheat650_to_whole__gte=0),
                                              name='650 type wheat flour to whole flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(wheat2000_to_whole__gte=0),
                                              name='2000 type wheat flour to whole flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(rye720_to_whole__gte=0),
                                              name='720 type rye flour to whole flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(rye2000_to_whole__gte=0),
                                              name='2000 type rye flour to whole flour ratio cannot be negative'),
                       models.CheckConstraint(check=models.Q(spelt650_to_whole__gte=0),
                                              name='650 type spelt flour to whole flour ratio cannot be negative')]


class ProcessBaking(models.Model):

    baking = models.ForeignKey(Bakings, on_delete=models.CASCADE, verbose_name="Name of baking")
    preparing_prefermentor_first = models.PositiveIntegerField("Duration of first prefermentation in minutes", default=720)
    preparing_prefermentor_second = models.PositiveIntegerField("Duration of second prefermentation in minutes", default=180)
    stretch_fold_count = models.PositiveIntegerField("Number of strech&fold reps", default=4)
    growing = models.PositiveIntegerField("Duration of dough growing in minutes", default=180)
    time_of_baking = models.PositiveIntegerField("Time of baking in minutes", default=50)
    temperature_of_baking = models.PositiveIntegerField("Temperature of baking in degrees of Celsius", default=200)

    def __str__(self):
        return self.baking


class EquipmentBaking(models.Model):

    baking = models.ForeignKey(Bakings, on_delete=models.CASCADE, verbose_name="Name of baking")
    bowl = models.BooleanField(default=True)
    silicone_spatula = models.BooleanField(default=True)
    oven = models.BooleanField(default=True)
    food_foil = models.BooleanField(default=True)
    scale = models.BooleanField(default=True)

    def __str__(self):
        return self.baking

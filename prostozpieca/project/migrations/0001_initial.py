# Generated by Django 3.1.6 on 2021-02-09 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentBaking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bowl', models.BooleanField(default=True)),
                ('silicone_spatula', models.BooleanField(default=True)),
                ('oven', models.BooleanField(default=True)),
                ('food_foil', models.BooleanField(default=True)),
                ('scale', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessBakings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparing_prefermentor_first', models.PositiveIntegerField(default=720)),
                ('preparing_prefermentor_second', models.PositiveIntegerField(default=180)),
                ('stretch_fold_count', models.PositiveIntegerField(default=4)),
                ('growing', models.PositiveIntegerField(default=180)),
                ('time_of_baking', models.PositiveIntegerField(default=50)),
                ('temperature_of_baking', models.PositiveIntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProportionBakings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('water_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('milk_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('salt_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('oil_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('butter_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sourdough_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('poolish_to_flour', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('wheat550_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('wheat00_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('wheat650_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('wheat2000_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('rye720_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('rye2000_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('spelt650_to_whole', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(water_to_flour__gte=0), name='Water to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(milk_to_flour__gte=0), name='Milk to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(salt_to_flour__gte=0), name='Salt to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(oil_to_flour__gte=0), name='Oil to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(butter_to_flour__gte=0), name='Butter to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(sourdough_to_flour__gte=0), name='Sourdough to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(poolish_to_flour__gte=0), name='Poolish to flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(wheat550_to_whole__gte=0), name='550 type wheat flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(wheat00_to_whole__gte=0), name='00 type wheat flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(wheat650_to_whole__gte=0), name='650 type wheat flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(wheat2000_to_whole__gte=0), name='2000 type wheat flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(rye720_to_whole_to_whole__gte=0), name='720 type rye flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(rye2000_to_whole_to_whole__gte=0), name='2000 type rye flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddConstraint(
            model_name='proportionbakings',
            constraint=models.CheckConstraint(check=models.Q(spelt650_to_whole_to_whole_to_whole__gte=0), name='650 type spelt flour to whole flour ratio cannot be negative'),
        ),
        migrations.AddField(
            model_name='processbakings',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.proportionbakings'),
        ),
        migrations.AddField(
            model_name='equipmentbaking',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.proportionbakings'),
        ),
    ]

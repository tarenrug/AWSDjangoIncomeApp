# Generated by Django 3.0.8 on 2020-08-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0007_auto_20200825_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeexpenditurestatement',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
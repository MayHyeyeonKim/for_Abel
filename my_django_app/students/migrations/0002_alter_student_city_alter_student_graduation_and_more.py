# Generated by Django 4.1.5 on 2023-03-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='graduation',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]
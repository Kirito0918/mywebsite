# Generated by Django 3.0.3 on 2020-02-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentalresult',
            name='post',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='experimentalresult',
            name='response',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='experimentalresult',
            name='result',
            field=models.CharField(max_length=600),
        ),
    ]

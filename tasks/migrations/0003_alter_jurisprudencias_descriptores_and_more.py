# Generated by Django 4.2.2 on 2023-06-21 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_jurisprudencias_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='descriptores',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='nombreProyecto',
            field=models.CharField(max_length=500),
        ),
    ]

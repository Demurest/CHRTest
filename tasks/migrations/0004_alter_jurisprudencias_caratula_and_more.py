# Generated by Django 4.2.2 on 2023-06-21 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_jurisprudencias_descriptores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='caratula',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='rol',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='tipoCausa',
            field=models.CharField(max_length=500),
        ),
    ]

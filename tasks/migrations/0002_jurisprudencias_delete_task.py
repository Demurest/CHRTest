# Generated by Django 4.2.2 on 2023-06-21 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisprudencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCausa', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
                ('caratula', models.CharField(max_length=100)),
                ('nombreProyecto', models.CharField(max_length=250)),
                ('descriptores', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]

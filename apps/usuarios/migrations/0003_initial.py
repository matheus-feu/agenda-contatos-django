# Generated by Django 4.1.7 on 2023-03-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('senha2', models.CharField(max_length=50)),
            ],
        ),
    ]

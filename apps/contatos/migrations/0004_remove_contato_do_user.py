# Generated by Django 4.1.7 on 2023-02-27 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_rename_mostrar_contato_publicada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='do_user',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-01 05:25

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0010_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='Avatars/%Y/%m/%d/', variations={'thumbnail': {'crop': True, 'height': 200, 'width': 200}}, verbose_name='Avatar'),
        ),
    ]

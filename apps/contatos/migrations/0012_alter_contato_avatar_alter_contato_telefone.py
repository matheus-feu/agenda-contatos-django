# Generated by Django 4.1.7 on 2023-03-01 07:53

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0011_alter_contato_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='Avatars/%Y/%m/%d/', variations={}, verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
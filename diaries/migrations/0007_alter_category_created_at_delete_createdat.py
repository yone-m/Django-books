# Generated by Django 4.1 on 2022-09-19 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0006_createdat_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
        migrations.DeleteModel(
            name='CreatedAt',
        ),
    ]

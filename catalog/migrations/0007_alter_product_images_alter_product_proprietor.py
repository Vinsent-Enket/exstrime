# Generated by Django 4.2 on 2024-01-25 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0006_alter_product_proprietor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, default='apu-upal-i-uronil-edu.jpg', null=True, upload_to='product/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='proprietor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
# Generated by Django 4.2.9 on 2024-01-20 13:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Заголовок поста')),
                ('slug', models.CharField(blank=True, default='djangodbmodelsfieldscharfield', max_length=150, null=True, verbose_name='Слаг')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью')),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Было опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
                'ordering': ('header', 'date_of_creation'),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('description', models.CharField(max_length=250, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('description',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название товара')),
                ('description', models.CharField(max_length=250, verbose_name='Описание товара')),
                ('images', models.ImageField(blank=True, default='apu-upal-i-uronil-edu', null=True, upload_to='product/', verbose_name='Картинка')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('date_of_change', models.DateField(default=django.utils.timezone.now, verbose_name='Дата изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('description',),
            },
        ),
    ]
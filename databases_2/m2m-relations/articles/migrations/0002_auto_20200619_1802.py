# Generated by Django 2.2.10 on 2020-06-19 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ArticleShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основная категория')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.Article', verbose_name='Статья')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.Scope', verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.ArticleShip', to='articles.Scope'),
        ),
    ]

# Generated by Django 2.2.10 on 2020-06-25 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_main_scope_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleship',
            options={'ordering': ('-is_main', 'scope__name')},
        ),
    ]

# Generated by Django 3.2.7 on 2022-03-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

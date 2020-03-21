# Generated by Django 3.0.4 on 2020-03-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirects_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirectinfo',
            name='browser',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='redirectinfo',
            name='os',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='redirectinfo',
            name='platform',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='redirectinfo',
            name='redirect_get_paramenters',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='redirectinfo',
            name='referrer_domain_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='redirectinfo',
            name='referrer_full_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]

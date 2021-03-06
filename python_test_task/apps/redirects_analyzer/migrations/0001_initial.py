# Generated by Django 3.0.4 on 2020-03-21 08:22

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('redirect_full_url', models.URLField(max_length=500)),
                ('redirect_domain_name', models.CharField(max_length=100)),
                ('redirect_get_paramenters', models.CharField(max_length=500)),
                ('referrer_full_url', models.URLField(max_length=500)),
                ('referrer_domain_name', models.CharField(max_length=100)),
                ('ip_address', models.GenericIPAddressField()),
                ('browser', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]

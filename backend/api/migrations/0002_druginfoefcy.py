# Generated by Django 4.1.6 on 2023-02-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugInfoEfcy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(default='', max_length=200, null=True)),
                ('item_name', models.CharField(default='', max_length=200, null=True)),
                ('item_seq', models.IntegerField(null=True)),
                ('efcy', models.CharField(default='', max_length=1000, null=True)),
                ('use_method', models.CharField(default='', max_length=1000, null=True)),
                ('atpn_warn', models.CharField(default='', max_length=1000, null=True)),
                ('atpn_esitm', models.CharField(default='', max_length=1000, null=True)),
                ('intrc_esitm', models.CharField(default='', max_length=1000, null=True)),
                ('se_esitm', models.CharField(default='', max_length=1000, null=True)),
                ('deposit', models.CharField(default='', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'use_method',
            },
        ),
    ]

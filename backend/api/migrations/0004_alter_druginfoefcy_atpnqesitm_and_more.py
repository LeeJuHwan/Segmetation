# Generated by Django 4.1.6 on 2023-02-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_atpn_esitm_druginfoefcy_atpnqesitm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='druginfoefcy',
            name='atpnQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='druginfoefcy',
            name='atpnWarnQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='druginfoefcy',
            name='depositMethodQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='druginfoefcy',
            name='efcyQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='druginfoefcy',
            name='intrcQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='druginfoefcy',
            name='seQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='druginfoefcy',
            name='useMethodQesitm',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
    ]

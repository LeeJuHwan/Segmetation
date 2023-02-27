# Generated by Django 4.1.6 on 2023-02-27 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_druginfoefcy_atpnqesitm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ITEM_SEQ', models.CharField(max_length=100)),
                ('ITEM_NAME', models.CharField(blank=True, default='', max_length=5000)),
                ('ENTP_NAME', models.CharField(blank=True, default='', max_length=5000)),
                ('ITEM_PERMIT_DATE', models.CharField(blank=True, default='', max_length=5000)),
                ('ETC_OTC_CODE', models.CharField(blank=True, default='', max_length=5000)),
                ('CLASS_NO', models.CharField(blank=True, default='', max_length=5000)),
                ('CHART', models.CharField(blank=True, default='', max_length=5000)),
                ('BAR_CODE', models.CharField(blank=True, default='', max_length=5000)),
                ('MATERIAL_NAME', models.CharField(blank=True, default='', max_length=5000)),
                ('EE_DOC_ID', models.CharField(blank=True, default='', max_length=5000)),
                ('UD_DOC_ID', models.CharField(blank=True, default='', max_length=5000)),
                ('NB_DOC_ID', models.CharField(blank=True, default='', max_length=5000)),
                ('INSERT_FILE', models.CharField(blank=True, default='', max_length=5000)),
                ('STORAGE_METHOD', models.CharField(blank=True, default='', max_length=5000)),
                ('VALID_TERM', models.CharField(blank=True, default='', max_length=5000)),
                ('REEXAM_TARGET', models.CharField(blank=True, default='', max_length=5000)),
                ('REEXAM_DATE', models.CharField(blank=True, default='', max_length=5000)),
                ('PACK_UNIT', models.CharField(blank=True, default='', max_length=5000)),
                ('EDI_CODE', models.CharField(blank=True, default='', max_length=5000)),
                ('CANCEL_DATE', models.CharField(blank=True, default='', max_length=5000)),
                ('CANCEL_NAME', models.CharField(blank=True, default='', max_length=5000)),
                ('TYPE_CODE', models.CharField(blank=True, default='', max_length=5000)),
                ('TYPE_NAME', models.CharField(blank=True, default='', max_length=5000)),
                ('CHANGE_DATE', models.CharField(blank=True, default='', max_length=5000)),
            ],
            options={
                'db_table': 'material',
            },
        ),
    ]
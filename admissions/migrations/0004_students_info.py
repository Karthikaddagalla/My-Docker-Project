# Generated by Django 3.2.7 on 2022-06-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_auto_20220620_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students_info',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('class_name', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
                ('amount_fee_paid', models.IntegerField(default=0)),
                ('date_of_admission', models.DateTimeField(auto_now=True)),
                ('Roll_no', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]

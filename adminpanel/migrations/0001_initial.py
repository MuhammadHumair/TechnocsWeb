# Generated by Django 3.0.8 on 2020-07-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=200)),
                ('isActive', models.BooleanField()),
            ],
            options={
                'db_table': 'Faqs',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('inquiryDate', models.DateField(auto_now=True)),
                ('dealedDate', models.DateField(blank=True, null=True)),
                ('isDealed', models.BooleanField()),
            ],
            options={
                'db_table': 'Inquiry',
            },
        ),
    ]

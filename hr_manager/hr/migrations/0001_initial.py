# Generated by Django 5.1.4 on 2025-01-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateField()),
                ('contract_length', models.IntegerField(help_text='Contract length in months')),
                ('contract_end', models.DateField()),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('STAFF', 'Staff')], max_length=20)),
            ],
        ),
    ]
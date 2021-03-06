# Generated by Django 2.1.7 on 2019-03-19 16:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190319_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('To', models.CharField(max_length=30)),
                ('Amount', models.IntegerField()),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.BankUser')),
            ],
        ),
    ]

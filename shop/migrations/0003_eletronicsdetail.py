# Generated by Django 4.2 on 2023-04-27 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_eletronics_actual_price_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='eletronicsdetail',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.TextField(default='', verbose_name='grapg')),
                ('href', models.TextField(default='', verbose_name='link')),
                ('eletronics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.eletronics')),
            ],
        ),
    ]
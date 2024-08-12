# Generated by Django 4.2.5 on 2023-10-02 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='code',
            field=models.CharField(default='<h5><span class="badge bg-primary ms-2">New</span></h5>', max_length=700),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_type', to='App.badge'),
        ),
    ]

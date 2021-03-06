# Generated by Django 3.2.9 on 2021-12-08 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_alter_item_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auth.user'),
            preserve_default=False,
        ),
    ]

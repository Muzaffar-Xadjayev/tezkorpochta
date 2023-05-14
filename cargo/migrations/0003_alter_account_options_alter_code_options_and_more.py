# Generated by Django 4.0.10 on 2023-05-11 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_alter_account_options_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Foydalanuvchilar', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
        migrations.AlterModelOptions(
            name='code',
            options={'verbose_name': 'Bir martalik parollar', 'verbose_name_plural': 'Bir martalik parollar'},
        ),
        migrations.CreateModel(
            name='SessionIdForAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sessiya id',
                'verbose_name_plural': 'Sessiya idlar',
            },
        ),
    ]
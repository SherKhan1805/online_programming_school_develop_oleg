# Generated by Django 4.2.10 on 2024-03-23 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0004_module_update_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now=True, verbose_name='дата платежа')),
                ('payment_amount', models.IntegerField(blank=True, null=True, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод')], max_length=50)),
                ('payment_session_id', models.CharField(blank=True, max_length=1000, null=True, verbose_name='идентификатор сессии платежа')),
                ('payment_status', models.CharField(blank=True, choices=[('successes', 'Успешно'), ('failed', 'Неуспешно')], max_length=50, null=True)),
                ('payment_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='курс оплаченный')),
                ('payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]

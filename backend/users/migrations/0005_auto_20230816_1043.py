# Generated by Django 3.2 on 2023-08-16 07:43

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230816_1037'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subscriptions',
            name='\nПодписка на себя.\n',
        ),
        migrations.AddConstraint(
            model_name='subscriptions',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, author=django.db.models.expressions.F('user')), name='Подписка на себя.'),
        ),
    ]

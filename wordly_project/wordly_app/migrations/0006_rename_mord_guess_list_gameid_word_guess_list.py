# Generated by Django 4.0.3 on 2022-03-12 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordly_app', '0005_gameid_mord_guess_list_alter_gameid_game_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameid',
            old_name='mord_guess_list',
            new_name='word_guess_list',
        ),
    ]

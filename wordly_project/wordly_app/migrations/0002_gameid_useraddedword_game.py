# Generated by Django 4.0.3 on 2022-03-12 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordly_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameID',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('game_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='useraddedword',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wordly_app.gameid'),
            preserve_default=False,
        ),
    ]
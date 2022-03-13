from django.db import models

# Create your models here.


class AddedWord(models.Model):

	id = models.AutoField(primary_key = True)
	addedword = models.CharField(max_length=5, unique = True)

	class meta:
		db_table = 'added_word'


class GameID(models.Model):

	id = models.AutoField(primary_key=True)
	game_id = models.CharField(max_length=100, unique=True)
	word_guess_list  = models.JSONField()
	class meta:
		db_table = 'game_id'

class UserAddedWord(models.Model):

	id = models.AutoField(primary_key=True)
	userword = models.JSONField()
	game = models.ForeignKey(GameID, on_delete = models.CASCADE)
	class meta:
		db_table = 'user_word'
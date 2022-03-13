import enchant # To check if word present in english dictionary
import docx2txt # To convert document to text
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


list_check = ['', " ", None, "null"]
eng_dict = enchant.Dict('en_us') # Iherit proporty of enchant

# Function  to add word to db using doc file
def add_word():
	text = docx2txt.process(r'C:\Users\user\Downloads\5letters.docx')
	for word in text.splitlines():
		try:
			AddedWord.objects.create(addedword=word)
		except Exception as e:
			print(f"{e}")

# To begin the game
class StartPlay(APIView):

	def post(self,request):
		word_list = list(AddedWord.objects.order_by('?')[0:5].values_list('addedword'))
		game_word_list  = []
		for word in word_list:
			word = list(word)
			for char in word:
				game_word_list.append([cha.upper() for cha in char])
		game_id = uuid.uuid4() # Unique Id for every game
		word_guess_list = game_word_list # List of word to match the word
		GameID.objects.create(game_id=game_id,word_guess_list=word_guess_list )
		return Response({"status":True, "message":{}, "data":{"game_id":game_id}, "word_guess_list":word_guess_list}) #Word Guess list can be removed . Here just to check


# To check whether the user guessing right word or not

class WordPlayView(APIView):
	
	def post(self, request):
		data = request.data
		word_list = data.get('userword')
		game_id = data.get('game_id')
		index_value = 0
		return_list = []
		mesasage  = ""
		try:
			game_data = GameID.objects.get(game_id=game_id)
			word_guess_list = game_data.word_guess_list
		except :
			return Response({"status":False, "message":{"game_id":f"Given gameid {game_id} is incorrect"}, "data":{'word_list':return_list},"user_list":word_list})
		if word_list in list_check:
			return Response({"status":False, "message":{"type":f'data cannot be {world_list}'}, "data":{'word_list':return_list,"user_list":word_list}})
		if type(word_list) != list:
			return Response({"status":False, "message":{"type":f"userword cannot be of type {type(word_list).__name__}"}})
		if len(word_list) != 5:
			return Response({"status":False, "message":{'length':'Length should be 5'}, "data":{'word_list':return_list,"user_list":word_list}})
		for word in word_list:
			word_guess = word_guess_list[index_value]
			word_string = ('').join(word)
			if type(word) != list:
				status = False
				message = f"Cannot be of type {type(word).__name__}"
				break

			if len(word) < 5 and word != [] :
				status = False
				message = "Length is short"
				return_list.append([{"word":char.upper(), "color":"Grey"} for char in word])
				break
			elif len(word) >5 and word != []:
				status = False
				message = "Length is long"
				return_list.append([{"word":char.upper(), "color":"Grey"} for char in word])
				break
			elif word ==[]:
				break
			elif word ==  word_guess:
				return_list.append([{"word":char.upper(), "color":"Green"} for char in word])
				message = "Word Match...!!!"
				status = True
			elif word != word_guess:
				if len(word_string)> 5:
					status = False
					message="Word is long"
					return_list.append([{"word":char.upper(), "color":"Grey"} for char in word])
					break
				elif len(word_string) < 5:
					status = False
					message = "Length is Short"
					return_list.append([{"word":char.upper(), "color":"Grey"} for char in word])
					break
				try:
					AddedWord.objects.get(addedword__icontains=word_string)
					message = "Word Match"
					return_list.append([{"word":char.upper(), "color":"Grey"} for char in word])
					status = True
				except:
					if eng_dict.check(word_string) and len(word_string) == 5:
						status = False
						message= "Thanks for adding new word to our dictionary..!!"
						AddedWord.objects.create(addedword=word_string)
						return_list.append([{"word":char.upper(), "color":"Grey"} for char in word])
					else:
						message = "No Such Word"
						status = False
						word_list = []
						for wordinlist1,wordinlist2 in zip(word, word_guess):
							if wordinlist1 == wordinlist2:
								word_list.append({"word":wordinlist1.upper(), "color":"Green"})
							elif wordinlist1 in word_guess:
								word_list.append({"word":wordinlist1.upper(), "color":"Yellow"})
							else:
								word_list.append({"word":wordinlist1.upper(), "color":"Grey"})
						if word_list != []:
							return_list.append(word_list)
			index_value += 1
		return Response({"status":status, "message":{"error":message}, "data":{"word_list":return_list}})


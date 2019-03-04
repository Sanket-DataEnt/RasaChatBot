from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionRequest(Action):
	def name(self):
		return 'action_req_type'
		
	def run(self, dispatcher, tracker, domain) :
		req = tracker.get_slot('req')

		if (req == 'order'):
			#print('HELLO')
			res = 'Thanks for choosing us. What would you like to eat?'
		elif (req == 'customer care'):
			res = 'Sorry for the inconvenience. Please leave your phone number, our agent will contact you.'
		else:
			#print("BHAG")
			res = 'Wrong Choice'
			
			#response = """In {} currently we have {}""".format(food, res)
		dispatcher.utter_message(res)
		return[]
		

class ActionNveg(Action):
	def name(self):
		return 'action_nveg_type'
		
	def run(self, dispatcher, tracker, domain) :
		vegn = tracker.get_slot('vegn')
		food = tracker.get_slot('food')
		print(food)
		#print("FAASOS")
				
		if (food == 'indian') & (vegn == 'vegetarian'):
			#print('HELLO')
			res = 'Aloo Paratha'
		elif (food == 'indian') & (vegn == 'non - vegetarian'):
			res = 'Chicken-Biryani'
		elif (food == 'chinese') & (vegn == 'vegetarian'):
			res = 'noodles'
		elif (food == 'chinese') & (vegn == 'non - vegetarian'):
			res = 'Chicken-Noodles'
		elif (food == 'italian') & (vegn == 'vegetarian'):
			res = 'Pizza'
		elif (food == 'italian') & (vegn == 'non - vegetarian'):
			res = 'Chicken Overloaded cheese Pizza'
		elif (food == 'dessert') & (vegn == 'vegetarian'):
			res = 'ice-cream'
		elif (food == 'dessert') & (vegn == 'non - vegetarian'):
			res = 'Egg-Cake'
		else:
			#print("BHAG")
			res = 'Wrong Choice'
			
			#response = """In {} currently we have {}""".format(food, res)
		dispatcher.utter_message(res)
		return[]
		

class ActionDisplayMenu(Action):
	def name(self):
		return 'action_menu_type'
		
	def run(self, dispatcher, tracker, domain) :
		#food = tracker.get_slot('food')
		#print(food)
		#print("FAASOS")
		import datetime as dt
		import pandas as pd
		time = dt.datetime.now()
		time = pd.to_datetime(time)
		h = time.hour
		m = time.minute
		t = m + (h*60)
		if (t>=300) & (t<=660):
			res = ("Here's the menu for breakfast today :\n 1.Indian \n 2.Chinese \n 3.Italian \n 4.Dessert")
		elif (t>=661) & (t<=960):
			res = ("Here's the menu for lunch today :\n 1.Indian \n 2.Chinese \n 3.Italian \n 4.Dessert")
		elif (t>=961) & (t<=1140):
			res = ("Here's the menu for snacks today :\n 1.Indian \n 2.Chinese \n 3.Italian \n 4.Dessert")
		elif (t>=1141):
			res = ("Here's the menu for dinner today :\n 1.Indian \n 2.Chinese \n 3.Italian \n 4.Dessert")
		else:
			#print("BHAG")
			res = 'No Food'
			
			#response = """In {} currently we have {}""".format(food, res)
		dispatcher.utter_message(res)
		return[]

		
class ActionSelectCuisine(Action):
	def name(self):
		return 'action_cuisine_type'
		
	def run(self, dispatcher, tracker, domain) :
		cuisine = tracker.get_slot('cuisine')
		#print("FAASOS")
		
		
		if cuisine == 'aloo paratha':
			#print('HELLO')
			res = 'Can I confirm your order?'
		elif cuisine == 'chicken - biryani':
			res = 'Can I confirm your order?'
		elif cuisine == 'noodles':
			res = 'Can I confirm your order?'
		elif cuisine == 'chicken - noodles':
			res = 'Can I confirm your order?'
		elif cuisine == 'pizza':
			res = 'Can I confirm your order?'
		elif cuisine == 'chicken overloaded cheese pizza':
			res = 'Can I confirm your order?'
		elif cuisine == 'ice - cream':
			res = 'Can I confirm your order?'
		elif cuisine == 'egg - cake':
			res = 'Can I confirm your order?'
		else:
			#print("BHAG")
			res = 'No Food for now'
			
			#response = """In {} currently we have {}""".format(food, res)
		dispatcher.utter_message(res)
		return[]
		
		
			
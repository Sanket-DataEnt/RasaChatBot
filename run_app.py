from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-3787543512-350934098721-539256742071-7724937e1d8546e6848b18d164f7ce09', #app verification token
							'xoxb-3787543512-539614799910-QTsNHySAzoEzm8PW1QNd1te4', # bot verification token
							'pgr4D9oUouYTEPL74l3vZGAW', # slack verification token
							True) #bug mode True

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

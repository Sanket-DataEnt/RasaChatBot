# RasaChatBot
Small Food Ordering Chat Bot using RASA

## Basic RASA Dependencies
Using RASA NLU version 0.14.1
Using RASA Core version 0.9.0a2

## Steps
Clone the repo
1. Install Anaconda3
2. Create Environment and install requirements and activate the environment

$conda create --name <env-name> --file requirements.txt
  
3. Run the python trainer.py train-all to train the model.
4. Run the python train_online.py to train the model and correcting the mistakes of the model.
5. Finally run the python bot.py.

## Overview of the files
data/core/ - contains stories for Rasa Core

data/nlu - contains example NLU training data

domain.yml - the domain file for Core

nlu-config.yml - the NLU config file

policy.yml - the Core config file

actions.py - the action against intents

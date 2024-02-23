#!/Users/arooshasolomon/opt/anaconda3/bin/python3

import os

SOCCR_T = input('What is your favroite soccer team? ')
ETHNC = input('What is your ethnicity? ')
FAVORITE_FOOD= input('What is your favorite food?' )


os.environ["SOCCR_T"] = SOCCR_T
os.environ["ETHNC"] = ETHNC
os.environ["FAVORITE_FOOD"] = FAVORITE_FOOD


SOCCR_T_ENV = os.getenv("SOCCR_T")
ETHNC_ENV = os.getenv("ETHNC")
FAV_FO_ENV = os.getenv("FAVORITE_FOOD") 

print(SOCCR_T_ENV, ETHNC_ENV , FAV_FO_ENV)


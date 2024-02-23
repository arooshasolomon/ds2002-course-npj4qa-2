#!/bin/bash

clear
echo "Let's build a mad-lib!"

# Prompt user for each input silently
read  -p "1. Please give me an adverb indicating a specific point in time: " ADVRB1
read  -p "2. Please give me a preposition indicating location or relationship in time: " PRED1
read  -p "3. Please give me an article: " ARTC
read  -p "4. Please give me a noun: " NOUN1
read  -p "5. Please give me an adverb or pronoun: " ADVRB2
read  -p "6. Please give me a verb: " VRB1
read -p "7. Please give me another adverb: " ADVRB3
read -p "8. Please give me a noun: " NOUN2
read -p "9. Please give me a verb: " VRB2
read -p "10. Please give me a preposition, indicating location or position: " PRED2
read -p "11. Please give me an adjective: " ADJ3
read -p "12. Please give me a noun : " NOUN3


# Echo out the mad-lib
echo "$ADVRB1 $PRED1 $ARTC $NOUN1 $ADVRB2 $VRB1 $ADVRB3 $NOUN2 $VRB2 $PRED2 $ADJ3 $NOUN3"


	

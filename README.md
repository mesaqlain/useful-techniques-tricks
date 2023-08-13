# Useful Techniques & Tricks
This is an ongoiong repository containing various simple techniques and tricks I've used for different projects.

## [Sort by different keys](https://github.com/mesaqlain/useful-techniques-tricks/blob/main/sort_dbz_cards.py)
### Problem:
* I have a text file containing the names of cards from the mobile game DBZ Dokkan Battle. Each name is in a new line and has the same format. The first three letters specify the type of the card (AGL, STR, PHY, INT, TEQ), followed by a space. The next two letters specify the rarity of the card (UR and LR), followed by a space. The remaining part of the string is the name of the card in question.
* The goal is to sort this file first based on the type and then by the rarity (a third key could also be added to then sort by the actual card name).
### Functions:
* Read the .txt file and extract each new line as a string in a list
* Create a custom key based on our indices
* Sort the lines
* Write the sorted lines in a new file
### Requirements:
None



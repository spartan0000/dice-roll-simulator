#dice roll
#ask how many dice they want to roll


import random

dice_images = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
	
#need sizes of the above
#this is the length of the first image which is the number of rows and is therefore the height
height = len(dice_images[1])
#this is the length of the first row of the first image which is, therefore, the width of the image
length = len(dice_images[1][0])
#needs some space when we print the dice images side by side
separator = " "

def convert_input(numberRoll):

	if numberRoll.strip() in {'1', '2', '3', '4', '5', '6'}:
		return int(numberRoll)
	else:
		print('Please enter a number between 1 and 6')
		numberRoll = input("How many dice do you want to roll? (1-6)  ")
		#raise SystemExit(1)

def roll(numberRoll):

	#will create a list with the result of each dice that is rolled
	numberRoll = int(numberRoll)
	roll_result = []
	for i in range(numberRoll):
		roll = random.randint(1,6)
		roll_result.append(roll)
	return roll_result
	
def make_dice_face(rollValues):
	dieFaces = _getDiceFaces(rollValues)
	dieFacesRows = _getDieFacesRows(dieFaces)
	
	
	dieFacesDiagram = "\n".join(dieFacesRows)
	return dieFacesDiagram


def _getDiceFaces(rollValues):
	dieFaces = []
	for i in rollValues:
		dieFaces.append(dice_images[i])
	return dieFaces

	#need to break dice images into individual rows and append them row by row by iterating over the 'height'
def _getDieFacesRows(dieFaces):
	dieFacesRows = []
	for row in range(height):
		row_items = []
		for die in dieFaces:
			row_items.append(die[row])
		#adds the separator (space) between rows to create space between dice images
		row_string = separator.join(row_items)

		dieFacesRows.append(row_string)
	return dieFacesRows
	

numberRoll = input('How many dice do you want to roll? (1-6)  ')
numberRoll = convert_input(numberRoll)
roll_result = roll(numberRoll)
#print(roll_result) #for testing the above code only

diagram = make_dice_face(roll_result)

print(f"\n{diagram}")



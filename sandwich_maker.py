#! python3
# sandwich_maker.py - Ask the user for a sandwich preference.

import pyinputplus as pyip

# Cost of the ingredients
prices = {'wheat': 10,
          'white': 7,
          'sourdough': 15,
          'chicken': 40,
          'turkey': 55,
          'ham': 45,
          'tofu': 40,
          'cheddar': 15,
          'Swiss': 25,
          'mozzarella': 30,
          'mayo': 5,
          'mustard': 6,
          'lettuce': 8,
          'tomato': 7,
          'none': 0,
          }

print('====SANDWICH MAKER====')

print("Hi mam'sir, welcome to our restaurant. What's your order?")

while True:
    # Ask the customer for their sandwich choices.
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                           'What type of bread do you want?\n')

    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                             'What type of protein do you want?\n')

    cheese_choice = pyip.inputYesNo('Do you want cheese?\n')

    if cheese_choice == 'yes':
        cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
                                'What type of cheese do you want?\n')
    else:
        cheese = 'none'

    condiments = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'],
                                'What condiments do you want?\n')

    amount = pyip.inputInt('How many sandwiches?\n', min=1)

    # Calculate the total cost.
    total_cost = (prices[bread] + prices[protein] + prices[cheese]
                  + prices[condiments]) * amount

    # Different depending on if customer wanted cheese.
    if not cheese == 'none':
        print(f"""To recount your order:
   {amount} {bread} sandwiches with {protein},
   topped with {cheese} cheese and {condiments}.
   Total cost: {total_cost}.00 pesos.""")
    else:
        print(f"""To recount your order:
   {amount} {bread} sandwiches with {protein},
   topped with {condiments}.
   Total cost: {total_cost}.00 pesos.\n""")

    # Ask the customer if their order is right.
    right_order = pyip.inputYesNo('Is this the right order?\n')
    if right_order == 'no':
        print("Mam'sir, please restate your order...")
        continue
    else:
        print('Enjoy your meal!')
        break

# Interview Assesment
# Scenario
# Code a vending machine application that has 5 different beverages of different prices in RM, no coins.

# Outcome:
# The logic of the vending machine will be able to return the least amount of notes back to the customers.

import re
import time

class vending:
    inventory_vm = {1: {'name': 'Machiatto Chocolate Special', 'price': 20},
                    2: {'name': 'Latte Hazulnut', 'price': 15},
                    3: {'name': 'Expresso', 'price': 8},
                    4: {'name': 'Bubble Tea Cream', 'price': 16},
                    5: {'name': 'Mineral Water', 'price': 5}
                    }


    def __init__(self, user_input):
        self.user_input = user_input
        self.total_amount = 0
        self.RM_currency = ''
        self.RM_integer = 0


    def validate_input(self):

        RM_currency_pattern = r'([Rr]{1}[Mm]{1})\s*(\d*\.*\d*)'  #eg. RM100, support whitespace and not case sensitive
        check_currency = re.match(RM_currency_pattern, self.user_input)

        while True:
            if check_currency:  # if True (Not None)
                try:
                    RM_Currency = check_currency.group(1).upper()

                    #Integer only accept whole number. Any decimal (or float) will raise an error
                    RM_integer =  int(check_currency.group(2)) 

                    #Pass the value to the variables
                    self.RM_currency = RM_Currency 
                    self.RM_integer = RM_integer
                
                except Exception:
                    print('system cannot accept coin')
                    break

            return "System cannot read the note. Please ensure your note is valid"

        return "System stop"

    #Here is the process to show only available items based on user input
    def checking_available_items(self):
        self.validate_input() #run validation process
        amount = self.RM_integer
        if amount  == 0:
            print("Invalid amount or currency")
        else:
            print("Current amount = RM ", amount )
            print("Available item")
            for key, value in self.inventory_vm.items():
                item_no, item_name, item_price = key, value['name'], value['price']
                if amount >= item_price:
                    print(f'Item No: {item_no} --  Item Name: {item_name} -- RM {item_price}')
        return ''

    #Main process is here. This function will calculate the amount.
    def process(self) -> int:
        amount = self.RM_integer
        if amount == 0:
            print("Please ensure your note is valid (RM)\nSystem terminated!")
        else:
            user_choice = input("Please insert item no... Item No: ")
            for key, value in self.inventory_vm.items():
                item_no, item_name, item_price = key, value['name'], value['price']

                if int(user_choice) == item_no:
                    if amount >= item_price:
                        print(f"Current amount: RM {amount}\nyou have choose {item_name} = RM {item_price}")
                        self.total_amount = amount - item_price
                        print(f"Your balance is RM {self.total_amount}")
                        return f"Your balance is RM {self.total_amount}"
                
                    else:
                        print( 'Insufficient amount\n\n===============================================')
                        print('Please ONLY SELECT the item in the list!')
                        self.checking_available_items()
                        self.process()
                        return f"Your balance is RM {self.total_amount}"
        return "2"

    #Main objective of this assignment. This function will return the value the least amount of notes.
    def _return_remaining(self):
        current_amount = self.total_amount
        note_list = [50,20,10,5,1]
        note_store = {}
        if current_amount > 0:
            for note in note_list:
                calculate = current_amount // note
                current_amount -= note * calculate
                note_store[note] = calculate
            print(f'Total note = ', sum([value for value in note_store.values()]))
            return "".join([f'\n- RM {key} x {value}' for key, value in note_store.items()])

        return "1"
    
    #Compiling and execute all the process
    def main(self): 
        check_item = self.checking_available_items()
        run_process = self.process()
        run_returning_process = self._return_remaining()
        print(check_item) 
        time.sleep(1)
        print(run_process)
        time.sleep(1)
        print(run_returning_process)
        return 'Thank you!'


#Run the process
if __name__ == '__main__':
    print("""
=========================================================================  
    Hi there,
    Welcome to HPN Vending Machine.
    Please insert the note to begin.
=========================================================================              
Important Instruction:
    System only accept 'RM' (without case sensitive)
                     """)
    user_input = input("Please insert the note... ")
    run_vending = vending(user_input)
    operate_vending = run_vending.main()
    print(operate_vending)
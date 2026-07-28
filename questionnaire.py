import options

prompt = 'This is a short questionnaire to help you to invest your money.'
prompt += "\nLet's start!"
prompt += "\nWhat's your name? name:"

name = input(prompt)
name = name.title()

while True:
    try:
        age = int(input('How old are you? age:'))
        break
    except ValueError:
            print("Please enter a valid age.")
age = int(age)

def extra(age):       
    if age >= 13:      
        print("\nWould you like to find out how much you will save?")
        print("Enter 'no'if not. ")
        amount = input("If yes, enter the amount to invest\n(use dots if necessary) amount:")  

        if amount == 'no':
            print('The questionnaire has been finished.')
        else:
            try:
                float(amount)
                total = float(amount) * values
                total = round(total, 2)
                print(f"You will receive {total} after {period}.")
                print("Please notice, tax not included.")
            except ValueError:
                print("It isn't a value. The questionnaire has been finished.")
        
if age < 13 or age > 120:
    print(f"I'm so sorry {name}, users younger than 13 or older than 120 are excluded.")
elif age >= 18:
    additional_adults = input(
                            f"{name}, would you like the option to withdraw funds at any time" \
                            "\nwithout losing the accrued interest? " \
                            "\nPlease enter 'yes' or 'no':"
                            )
    
    if additional_adults == 'yes':
        options.adult_savings_account()
        percentage = float(options.adult_savings_account.__defaults__[1])
        period = 'one month'
        values = percentage/12/100
        extra(age)
    
       
    elif additional_adults == 'no':
        details = input("Would you prefer to invest for three months at 3,3% or for six months at 3,4%? \
                        \nPlease enter 'three' or 'six:")
        if details == 'three':
                    options.adult_deposit_three()
                    percentage = float(options.adult_deposit_three.__defaults__[1])
                    period = 'three months'
                    values = percentage*3/12/100
                    extra(age)
        elif details == 'six':
                    options.adult_deposit_six()
                    percentage = float(options.adult_deposit_six.__defaults__[1])
                    period = 'six months'
                    values = percentage*6/12/100
                    extra(age)
        else:
            print("Sorry, no response from your side. The questionnaire has been stopped.")

    else:
            print("Sorry, your answer was not valid. The questionnaire has been stopped.")
        
        
                        
else:
    additional_youngs = input(
                             f"{name}, would you like the option to withdraw funds at any time"
                             "\nwithout losing the accrued interest?"
                             "\nPlease enter 'yes' or 'no':"
                             )
    if additional_youngs == 'yes':
                             options.young_savings_account()
                             percentage = float(options.young_savings_account.__defaults__[1])
                             period = 'one month'
                             values = percentage/12/100
                             extra(age)
    elif additional_youngs == 'no':
                            options.young_deposit()
                            percentage = float(options.young_deposit.__defaults__[1])
                            period = 'three months'
                            values = percentage*3/12/100
                            extra(age)
    else:
        print("Sorry, no response from your side. The questionnaire has been stopped.")



    




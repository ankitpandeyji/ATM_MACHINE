import time 
print("Please insert your card!!")
time.sleep(7)

password=12345

pin = int(input("Please enter your ATM PIN "))

balance = 50000

if pin == password:
        while True :
            print("""""
                1 == Balance check 
                2 == Cash withdraw
                3 == Cash deposit
                4 == Exit
                """)
            try :
                option = int(input("Please select your option"))

            except:
                
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")                
                print("Enter valid option!!")
                
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

            if option == 1:
                print("****************************************************************************************************************")
                print(f"current balance is {balance}")
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

            if option == 2:
                withdraw_amt = int(input("Please enter withdraw_amt"))
                balance = balance - withdraw_amt
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

                print(f"{withdraw_amt} is debated from your account")
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

                print(f"Your updated balance is {balance}")
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

            if option == 3:
                deposit_amt = int(input("Please enter your deposit_amt"))

                balance = balance + deposit_amt
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

                print(f"{deposit_amt} is credit to your account.")
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

                print(f"Your updated balanc is{balance}")
                print("****************************************************************************************************************")
                print("****************************************************************************************************************")

            if option == 4:
                break
        else:
            
            print("Wroong PIN entered !! please enter valid PIN number..")
                

                                
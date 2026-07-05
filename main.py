import string
import random
import zxcvbn  

def check_strength_password(password):
    
    analyze = zxcvbn.zxcvbn(password)
    
    score = analyze['score']
    
    time_hack = analyze['crack_times_display']['online_no_throttling_10_per_second']
    
    suggestion_list = analyze['feedback']['suggestions']
    warning = analyze['feedback']['warning']
    
    print("\n=== PASSWORD ANALYSIS RESULTS ===")
    print(f"Your password: {password}")
    print(f"Length: {len(password)} characters")
    print(f"Estimated time to crack: {time_hack}")
    
    if warning:
        print(f"⚠️ Warning: {warning}")
    if suggestion_list:
        print("💡 Improvement suggestions:")
        for suggestion in suggestion_list:
            print(f"   - {suggestion}")
            
    if score == 0:
        return "❗ STRENGTH: VERY WEAK! (Very dangerous, this password can be hacked instantly!)"
    elif score == 1:
        return "🔴 STRENGTH: WEAK! (This password can be hacked easily)"
    elif score == 2:
        return "🟡 STRENGTH: MODERATE! (Not bad, but the password still has vulnerabilities)"
    elif score == 3:
        return "🟢 STRENGTH: STRONG! (This password is good and hard to crack)"
    elif score == 4:
        return "🛡️ STRENGTH: VERY STRONG! (Very strong, secure from hackers)"

def make_password_automation(length_req):
    character = string.ascii_letters + string.digits + string.punctuation
    new_password = ''.join(random.choice(character) for i in range(length_req))
    return new_password

while True: 
    print("\n=== SIMPLE PASSWORD SECURITY TOOLS ===")
    print("1. Check Password Strength")
    print("2. Generate Safe Password")
    print("3. Exit Program")
    choose = input("Choose menu (1/2/3): ")

    if choose == "1":
        while True:
            pwd = input("Input the password to be checked: ")
            if pwd == "" or " " in pwd:
                print("Password denied, cannot be empty or contain space !!!")
            else:
                print("Password confirmed, analyzing password...")
                results = check_strength_password(pwd)
                print(results)
                print("\nDo you want to try again? ")
                print("1. Yes")
                print("2. No")
                while True:
                    try:
                        option = int(input("Option (1/2): "))
                        if option == 1 or option == 2:
                            break
                        else:
                            print("Invalid input, please try again!")
                    except ValueError:
                        print("Input must be number 1 or 2!")     
                if option == 2:
                    break         
                    
    elif choose == "2":
        while True: 
            while True:
                try:   
                    length = int(input("How many characters do you want? (Recommendation: 15 characters): "))
                    if length > 64:
                        print("Password is too long, the maximum limit is 64 characters to maintain system security")
                    elif length < 12:
                        print("Password does not meet security standards. The recommended minimum length is 12 characters!")
                    else:
                        break
                except ValueError:
                    print("Invalid input, try again!")
            pwd_safe = make_password_automation(length)
            print(f"\nYour Secure Password: {pwd_safe}")
            print("Good luck with your Password :)")
            print("\nDo you want to try again? ")
            print("1. Yes")
            print("2. No")
            while True:
                try:
                    option = int(input("Option (1/2): "))
                    if option == 1 or option == 2:
                        break
                    else:
                        print("Invalid input, please try again!")
                except ValueError:
                    print("Input must be number 1 or 2!")
            if option == 2:
                break
                
    elif choose == "3":
        print("Thank you for trying our program! :)") 
        break
    else:
        print("Invalid input, please try again!") 

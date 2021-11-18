class PasswordValidator:
     def validate_password(self,userPassword):
            specialCharacter = ['@', '-','_', '+', '!', '?', '%', '$',"#"]
        #Passwords must be between 12 and 25 characters in length
            if len(userPassword) < 12:
                return "Fail"
            if len(userPassword) > 25:
                print("Password must be between 12 and 25 characters in length")
                return "Fail"
        #Passwords cannot contain the word 'password'
            if userPassword == 'password':
                print("Passwords cannot contain the word 'password'")
                return "Fail"
        #Passwords must contain at least 1 number, 1 capital letter and 1 of these special characters: @, -, _, +, !, ?, %, $, 
            if not any(char.isdigit() for char in userPassword):
                print("Passwords must contain at least 1 number")
                return "Fail"
            if not any(char.isupper() for char in userPassword):
                print("Passwords must contain at least 1 capital letter")
                return "Fail"
            if not any(char in specialCharacter for char in userPassword):
                print("Passwords must contain at least 1 of these special characters: @, -, _, +, !, ?, %, $")
                return "Fail"
        #Passwords cannot have 2 or more numbers or special characters in a row
            if userPassword.count('@') > 1 or userPassword.count('-') > 1 or userPassword.count('_') > 1 or userPassword.count('+') > 1 or userPassword.count('!') > 1 or userPassword.count('?') > 1 or userPassword.count('%') > 1 or userPassword.count('$') > 1:
                print("Password cannot have 2 or more special characters in a row")
                return "Fail"
            
        #Password cannot end with a number or Special Character
            if userPassword[-1] in specialCharacter or userPassword[-1].isdigit():
                print("Password cannot end with a number or special character")
                return "Fail"
        #Password must have at least 1 run of 5 or more letters in a sequence unless your password is more than 20 characters long
            if len(userPassword) > 20:
                return "Pass"
            else:
                for i in range(len(userPassword) - 4):
                    if userPassword[i] == userPassword[i+1] == userPassword[i+2] == userPassword[i+3] == userPassword[i+4]:
                        print("Password must have at least 1 run of 5 or more letters in a sequence")
                        return "Fail"
        #The  same single character must not repeat/ appear 4 or more times in a password
            count = {}
            for s in userPassword:
                if s in count:
                    count[s] += 1
            for key in count:
                if count[key]>4:
                    return "Fail"
            return "Pass"

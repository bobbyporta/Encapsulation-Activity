class PasswordChecker:
    def __init__(self):
        self._password = "admin" 
        self._attempts = 2  
        self._max_attempts = 2  

    def check_password(self, entered_password):
        return entered_password == self._password

    def run(self):
        while self._attempts >= 0:
            entered_password = input("Enter password: ")
            if self.check_password(entered_password):
                print("Access Granted! You may now enter.")
                break
            else:
                if self._attempts == 0:
                    print("You are now out of attempts.")
                elif self._attempts == 1:
                    print(f"You only have {self._attempts} attempt left.")
                else:
                    print(f"Access Denied! Invalid password.")
                    print(f"You only have {self._attempts} attempts left.")
            
            self._attempts -= 1
            print(" ")

def main():
    password_checker = PasswordChecker()
    password_checker.run()

if __name__ == "__main__":
    main()

class ZodiacSignCalculator:
    def __init__(self):
        self._month = 0
        self._date  = 0
        self._word_month = ["january", "february", "march", "april", "may", "june",
                            "july", "august", "september", "october", "november", "december"]

    def set_month(self, month):
        if 1 <= month <= 12:
            self._month = month
        else:
            print("INVALID MONTH!")

    def set_date(self, date):
        if 1 <= date <= 31:
            self._date = date
        else:
            print("INVALID DATE!")

    def get_zodiac_sign(self):
        
        if self._month == 0 or self._date == 0:
            print("Invalid input! Please enter valid month and date.")
            return

        
        month_name = self._word_month[self._month - 1].capitalize()
        if self._month == 1:  # January
            if 1 <= self._date <= 19:
                return f"Your zodiac sign is CAPRICORN ({month_name} {self._date})"
            elif 20 <= self._date <= 31:
                return f"Your zodiac sign is AQUARIUS ({month_name} {self._date})"
            

        elif self._month == 2: # February
            if 1 <= self._date <= 18:
                return f"Your zodiac sign is AQUARIUS ({month_name} {self._date})"
            elif 19 <= self._date <= 29:
                return f"Your zodiac sign is PISCES ({month_name} {self._date})"
            

        elif self._month == 3: # March
            if 1 <= self._date <= 20:
                return f"Your zodiac sign is PISCES ({month_name} {self._date})"
            elif 21 <= self._date <= 31:
                return f"Your zodiac sign is ARIES ({month_name} {self._date})"
            

        elif self._month == 4: # April
            if 1 <= self._date <= 19:
                return f"Your zodiac sign is ARIES ({month_name} {self._date})"
            elif 20 <= self._date <= 30:
                return f"Your zodiac sign is TAURUS ({month_name} {self._date})"
            

        elif self._month == 5:  # May
            if 1 <= self._date <= 20:
                return f"Your zodiac sign is TAURUS ({month_name} {self._date})"
            elif 21 <= self._date <= 31:
                return f"Your zodiac sign is GEMINI ({month_name} {self._date})"
            

        elif self._month == 6:  # June
            if 1 <= self._date <= 20:
                return f"Your zodiac sign is GEMINI ({month_name} {self._date})"
            elif 21 <= self._date <= 30:
                return f"Your zodiac sign is CANCER ({month_name} {self._date})"
            

        elif self._month == 7:  # July
            if 1 <= self._date <= 22:
                return f"Your zodiac sign is CANCER ({month_name} {self._date})"
            elif 23 <= self._date <= 31:
                return f"Your zodiac sign is LEO ({month_name} {self._date})"
            

        elif self._month == 8:  # August
            if 1 <= self._date <= 22:
                return f"Your zodiac sign is LEO ({month_name} {self._date})"
            elif 23 <= self._date <= 31:
                return f"Your zodiac sign is VIRGO ({month_name} {self._date})"
            

        elif self._month == 9:  # September
            if 1 <= self._date <= 22:
                return f"Your zodiac sign is VIRGO ({month_name} {self._date})"
            elif 23 <= self._date <= 30:
                return f"Your zodiac sign is LIBRA ({month_name} {self._date})"
            

        elif self._month == 10:  # October
            if 1 <= self._date <= 22:
                return f"Your zodiac sign is LIBRA ({month_name} {self._date})"
            elif 23 <= self._date <= 31:
                return f"Your zodiac sign is SCORPIO ({month_name} {self._date})"
            

        elif self._month == 11:  # November
            if 1 <= self._date <= 21:
                return f"Your zodiac sign is SCORPIO ({month_name} {self._date})"
            elif 22 <= self._date <= 30:
                return f"Your zodiac sign is SAGITTARIUS ({month_name} {self._date})"
            

        elif self._month == 12:  # December
            if 1 <= self._date <= 21:
                return f"Your zodiac sign is SAGITTARIUS ({month_name} {self._date})"
            elif 22 <= self._date <= 31:
                return f"Your zodiac sign is CAPRICORN ({month_name} {self._date})"
        else:
            return "INVALID INPUT!"

def main():
    zodiac_calculator = ZodiacSignCalculator()
    
    
    try:
        month = int(input("Enter your birth month in integer format: "))
        date = int(input("Enter your birth date: "))
        
        zodiac_calculator.set_month(month)
        zodiac_calculator.set_date(date)
        
        
        result = zodiac_calculator.get_zodiac_sign()
        if result:
            print(result)
    
    except ValueError:
        print("Invalid input! Please enter a valid integer for month and date.")

if __name__ == "__main__":
    main()

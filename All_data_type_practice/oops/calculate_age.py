from datetime import date


class AgeCalculate:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age


age_cal = AgeCalculate("Rajkumar", "india", date(1996, 6, 16))
print(age_cal.calculate_age())

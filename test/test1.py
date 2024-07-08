import sys

class Car:
    def __init__(self, color, company_name, year, model):
        self.color = color
        self.company_name = company_name
        self.year = year
        self.model = model

if len(sys.argv) == 5:
    color, company_name, year, model = sys.argv[1:5]
    print(color, company_name, year, model)
else:
    print('Usage: python script.py <color> <company_name> <year> <model>')

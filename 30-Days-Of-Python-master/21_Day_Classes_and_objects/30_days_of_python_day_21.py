import statistics as s

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class MeasureOfCentralTendencyOfsample:
    def __init__(self, data) -> None:
        self.mean = s.mean(data)
        self.median = s.median(data)
        self.mode = s.mode(data)
        self.range_variance = s.variance(data)
        self.std_derivation = s.stdev(data)
        self.sum = sum(ages)
        self.min = min(ages)
        self.max = max(ages)
    def print_data(self):
        print(f'mean: {self.mean}, median: {self.median}, mode: {self.mode}, range variance: {self.range_variance}, standard derivation: {self.std_derivation}, sum: {self.sum}, min: {self.min}, max: {self.max}.')

m1 = MeasureOfCentralTendencyOfsample(ages)

m1.print_data()


class PersonAccount:
    def __init__(self, firstname, lastname, incomes, incomes_dsecription, expenses, expenses_description) -> None:

        self.incomes_list = []
        self.expenses_list = []

        self.firstname = firstname
        self.lastname = lastname
        self.incomes = float(incomes)
        self.expenses = float(expenses)
        self.incomes_description = incomes_dsecription
        self.expenses_desciption = expenses_description

        self.incomes_list.append([incomes, incomes_dsecription])
        self.expenses_list.append([expenses, expenses_description])
    
    def add_operation(self):
        choice = int(input('Press 1 if yoou want to add an income, 2 if you want to add an expense, or 3 if you want to add both: '))

        if choice == 1:
            self.add_income = [float(input('Add income: ')), input('Add a description: ')]
            self.incomes_list.append(self.add_income)
        
        elif choice == 2:
            self.add_expenses = [float(input('Add expense: ')), input('Add a description: ')]
            self.expenses_list.append(self.add_expenses)
        
        elif choice == 3:
            self.add_income = [float(input('Add income: ')), input('Add a description: ')]
            self.incomes_list.append(self.add_income)
            self.add_expenses = [float(input('Add expense: ')), input('Add a description: ')]
            self.expenses_list.append(self.add_expenses)

        else: print('You haven\'t selected a valid operation')

    def show_incomes_or_expenses(self):

        choice = int(input('press 1 to see the incomes, 2 to see the expenses, 3 to see the account balance, 4 to see the every income or 5 to see every exepnse: '))

        if choice == 1: print(sum([element[0] for element in self.incomes_list]))
        elif choice == 2: print(sum([element[0] for element in self.expenses_list]))
        elif choice == 3: print(sum([element[0] for element in self.incomes_list]) - sum([element[0] for element in self.expenses_list]))
        elif choice == 4: print(self.incomes_list)
        elif choice == 5: print(self.exepnses_list)
        else: ('You haven\'t selected a valid operation.')

p = PersonAccount('N', 'S', 30000,'ingresos', 29999, 'taxes')

p.add_operation()

p.show_incomes_or_expenses()

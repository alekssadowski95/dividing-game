from random import randrange

class DivisionTask():
    def __init__(self, dividend, divisor, result):
        self.dividend = dividend
        self.divisor = divisor
        self.result = result
    
    def __repr__(self):
        return f'DivisionTask: divident={self.dividend}, divisor={self.divisor}, result={self.result}'

def create_random_division_task():   
    divisor = randrange(1, 9)
    result = randrange(1, 999)
    dividend = result * divisor
    division_task = DivisionTask(dividend=dividend, divisor=divisor, result=result)  
    return division_task

division_task = create_random_division_task()
print(division_task)
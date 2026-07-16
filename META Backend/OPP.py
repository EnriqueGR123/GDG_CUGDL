class Payslip:
    def __init__(self, name, payment, amout):
        self.name = name
        self.payment = payment
        self.amout = amout

    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment == 'yes':
            return f'{self.name } pago {str(self.amout)}'
        else:
            return f'{self.name} No ha pagao'


alan = Payslip('Alan', 'yes', '300')
juan = Payslip('juan', 'no', '20')
'''
print(alan.status())
print(juan.status())
'''




class empleado:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class chef(empleado):
    def __init__(self, name, last, password):
        super().__init__(name,last)
        self.password = password
    
class otro(empleado):
    def request(self, days):
        return f'{self.name} requested {days} days'
    

adrian = chef('adrian', 'otro','123')

adri = otro('adri', 'apellido')

print(adrian.password)

print(adri.request(3))



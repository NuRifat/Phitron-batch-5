class Phone:
    #this init method work as by default constructor in python
    def __init__(self, owner,price,model):
        self.owner = owner
        self.price = price
        self.model = model

rifat_phone = Phone('Rifat', 20000,'iPhone')
print(rifat_phone.owner,rifat_phone.price,rifat_phone.model)

arat_phone = Phone('Arat', 15000,'Samsung')
print(arat_phone.owner,arat_phone.price,arat_phone.model)

#ato boro kore jodi na likhe shudu rifat_phone likhe jodi sob output pete cahi tahole 'repr' use korte hobe

class New_phone():
    def __init__(self, owner,price,model):
        self.owner = owner
        self.price = price
        self.model = model
    def __repr__(self) -> str:
        return f'{self.owner} buys a new {self.model} mobile which price is {self.price}'
    
rifat = New_phone('Rifat', 54000, 'iPhone')
print(rifat)
safa = New_phone('Safa', 43000, 'Samsung')
print(safa)
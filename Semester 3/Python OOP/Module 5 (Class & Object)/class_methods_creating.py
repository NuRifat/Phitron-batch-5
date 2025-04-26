class Phone:
    #in every method or funtion in class their must a 'self' peremeter without value
    def call(self):
        print('Hello World! This is a class method')

my_phone = Phone()
my_phone.call()

#Another example using peremeters

class NewPhone:
    def send_sms(self, name):
        text = f'My name is {name}'
        return text
    
rifat_phone = NewPhone()
result = rifat_phone.send_sms('Rifat')
print(result)
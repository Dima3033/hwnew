class Phone:
    name = ''
    memory = ''
    ram = 0
    G = ''
    type = ''
    iphone = ''
    def __init__(self):
        print(f"Phone")
        self.name = "iPhone X"
        self.memory = '256GB'
        self.ram = 3
        self.G = '5,8'
        self.type = 'Smart Phone '
    def ShowOn(self):
        print(f"name: {self.name} \nmemory: {self.memory} \ndiagonal: {self.G} \ntype: {self.type} \nОЗП: {self.ram}")
    def __del__(self):
        print("deleted objects of phone")
if __name__ == '__main__':
    phone = Phone()
    phone.ShowOn()
    del phone
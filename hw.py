class Profession:
    name = ''
    framework = ''
    hours = ''

    def __init__(self):
        print(f"Profession")
        self.name = "Barista"
        self.framework = "12000"
        self.hours = '24/7'
    def ShowOn(self):
        print(f"Name: {self.name}  \nframework: {self.framework} \nhours: {self.hours}")
    def __del__(self):
        print("Deleted  profession")
if __name__ == '__main__':
    profession = Profession()
    profession.ShowOn()
    del profession
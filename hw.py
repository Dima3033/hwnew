class Musical:
    brand = ''
    variety = ''
    Keys = 0
    def __init__(self):
        print(f"Musical Instrument")
        self.brand = " Steinway & Sons"
        self.variety = 'keyboard instrument'
        self.Keys = 88
    def ShowOn(self):
        print(f"brand: {self.brand} \nvariety: {self.variety} \nKyes: {self.Keys}")
    def __del__(self):
        print("Deleted Musical Instrument")
if __name__ == '__main__':
    profession = Musical()
    profession.ShowOn()
    del Musical
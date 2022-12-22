class Post:
    name = ''
    position = ''
    size = ''
    type = ''
    def __init__(self):
        print(f"Post")
        self.name = "NOWA POSTA"
        self.position = 'Uria Klena 10'
        self.size = 'Enormous'
        self.type = 'Free'
    def ShowOn(self):
        print(f"name: {self.name} \nposition: {self.position} \nscale: {self.size} \ntype: {self.type}")
    def __del__(self):
        print("deleted objects of post")
if __name__ == '__main__':
    post = Post()
    post.ShowOn()
    del post
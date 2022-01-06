class player():
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print("hello", self.name.title())

    def intro(self):
        print("I am ok")


player1 = player("abc")
player1.sayHello()


class NbaPlayer(player):
    def __init__(self, name):
        super().__init__(name)
        self.category = name
    
    def intro(self):
        print(self.category.title())

player2 = NbaPlayer("vincent2")
player2.intro()
player2.sayHello() # Inheritant
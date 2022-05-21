class Human:
    def __init__(self, name):
        self.h = 180
        self.name = Valera
    def jump(self):
        print(f"Hello, I am {self.name}, I'm jumping")
    def run(self):
        print(f"Hello, I am {self.name}, I run")
        
class Spider:
    def __init__(self):
        self.w = 18
    def climb(self):
        print("Hello, I'm climb")
    def weaving(self):
        print(f"Hello, I weaving a web")
        
class SpiderMan(Human, Spider):
    def __init__(self, name):
        super().__init__(name)

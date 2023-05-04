
class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_word = "Winter is Coming"

    def print_house_words(self):
        print (self.house_word)

    def die(self):
        self.is_alive = False

    def __repr__(self):
        return (f"Stark({self.first_name}, {self.family_name}, {self.house_word},{self.is_alive})")

    
if __name__ == "__main__":
    arya = Stark("Arya", True)
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
    print(arya.__doc__)
    print(GotCharacter.__doc__)

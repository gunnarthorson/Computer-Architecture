class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.run())

print(player2.name)

def function(obj):
    count = 0
    for x in obj.values():
        if type(x) == int:
            count += x
    return count
  
obj = {"cat": "bob", "dog": 23, 19: 18, 90: "fish"} 
print(function(obj)) 
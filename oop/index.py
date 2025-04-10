from abc import ABC, abstractmethod

class Enemy:

    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @abstractmethod
    def __str__(self):
        pass


class Zombie(Enemy):

    def __init__(self, name, hp, atk, skill):
        super().__init__(name, hp, atk)
        self.skill = skill

    def __str__(self):
        return f"Name: {self.name.capitalize()}\nHealth: {self.hp}\nAttack: {self.atk}\nSkill: {self.skill}"



class FlyingZombie(Enemy):

    def __init__(self, name, hp, atk, special_skill):
        super().__init__(name, hp, atk)
        self.special_skill = special_skill

    def __str__(self):
        return f"Name: {self.name.capitalize()}\nHealth: {self.hp}\nAttack: {self.atk}\nSpecial Skill: {self.special_skill}"

zombie = Zombie("zomboss", "2500", "500 dmg", "bomba")
flying_zombie = FlyingZombie("zomfly", "1500", "1000 dmg", "deathcap")

print(zombie)
print()
print(flying_zombie)



# class A:
#     def __init__(self):
#         super().__init__()
#         self.prop1 = "Prop 1"

# class B:
#     def __init__(self):
#         super().__init__()
#         self.prop2 = "Prop 2"

# class C(A, B):

#     def call(self):
#         print(self.prop1)
#         print(self.prop2)

# c = C()

# c.call()



# Duck typing

# class Animal:
#     is_alive = True

# class Dog(Animal):
#     def make_sound(self):
#         print("Arf arf!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow meow")

# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.make_sound()
#     print(animal.is_alive)



# Polymorphism

# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 2 * 3.14 * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def area(self):
#         return (self.base * self.height) / 2

# class Pizza(Circle):
#     def __init__(self, radius, toppings):
#         super().__init__(radius)
#         self.toppings = toppings

# shapes = [Circle(5), Square(4), Triangle(6,7), Pizza(7, "Ham and cheese")]

# for shape in shapes:
#     print(f"{shape.area()}")



# from abc import ABC, abstractmethod

# class Enemy:
    
#     def __init__(self, name, health, atk_dmg):
#         self.name = name
#         self.health = health
#         self.atk_dmg = atk_dmg

#     @abstractmethod
#     def special_skill(self):
#         print(f"--- {self.name} ---")


# class Zombie(Enemy):

#     ss = "Chomp chomp"

#     def __init__(self, name, health, atk_dmg, energy):
#         super().__init__(name, health, atk_dmg)
#         self.energy = energy

#     def special_skill(self):
#         super().special_skill()
#         print(f"Special skill: {self.ss}")  

# class FlyingZombie(Enemy):

#     ss = "Dive chomp"

#     def __init__(self, name, health, atk_dmg, mana):
#         super().__init__(name, health, atk_dmg)
#         self.mana = mana

#     def special_skill(self):
#         super().special_skill()
#         print(f"Special skill: {self.ss}")


# zombie = Zombie("Zomboss", 1000, 500, 100)
# flying_zombie = FlyingZombie("Zomfly", 500, 1000, 80)

# zombie.special_skill()
# flying_zombie.special_skill()


# class Character:

#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk

# class Warrior(Character):

#     def __init__(self, name, hp, atk, shield):
#         super().__init__(name, hp, atk)
#         self.shield = shield

#     def special_ability(self):
#         print(f"{self.name} special ability is {self.shield}")

# class Healer(Character):

#     def __init__(self, name, hp, atk, wand):
#         super().__init__(name, hp, atk)
#         self.wand = wand


# warrior = Warrior(name="Pantheon", hp="3000", atk="500", shield="sterak")
# healer = Healer(name="Soraka", hp="1000", atk="100", wand="Healing")

# warrior.special_ability()

# print("======= CHARACTER 1 =======")
# print(f"Name   : {warrior.name}")
# print(f"Health : {warrior.hp}")
# print(f"Attack : {warrior.atk}")
# print(f"Shield : {warrior.shield}")
# print("===========================")

# print("======= CHARACTER 2 =======")
# print(f"Name   : {healer.name}")
# print(f"Health : {healer.hp}")
# print(f"Attack : {healer.atk}")
# print(f"Wand   : {healer.wand}")
# print("===========================")











# class Animal:

#     def eat(self):
#         print("This animal is eating")

#     def walk(self):
#         print("This animal is walking")

# class Prey(Animal):

#     def flee(self):
#         print("This animal is fleeing")

# class Predetor(Animal):
    
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predetor):
#     pass

# class Fish(Prey, Predetor):
#     pass


# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# fish.walk()

# rabbit.flee()
# hawk.hunt()






# class Enemy:

#     def __init__(self, name, hp, atk_dmg):
#         self.name = name
#         self.hp = hp
#         self.atk_dmg = atk_dmg
#         self.active = True

#     def basic_atk(self):
#         print(f"{self.name} is attacking...")
    
#     def walk(self):
#         print(f"{self.name} is walking...")

# class Zombie(Enemy):
    
#     def run(self):
#         print(f"{self.name} is running!")

# class FlyingZombie(Enemy):

#     def fly(self):
#         print(f"{self.name} is flying!")


# zombie = Zombie("Zomwalk", 5000, 500)
# flying_zombie = FlyingZombie("Zomfly", 3000, 800)

# zombie.basic_atk()
# zombie.walk()
# zombie.run()

# flying_zombie.basic_atk()
# flying_zombie.walk()
# flying_zombie.fly()
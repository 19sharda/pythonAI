# class Robot:
#     def __init__(self, name, battery_level,mob):
#         self.name = name
#         self.battery = battery_level
#         self.mob=mob
#     # A method to DO something
#     def introduce(self):
#         print(f"Hello! I am {self.name}.")
#
#         print(self.mob)
#
#     # A method to CHANGE data
#     def charge(self):
#         print("Charging...")
#         self.battery = 100  # Modifying the object's own data
#         self.mob = "mi"
#         print(self.mob)
# my_bot = Robot("Terminator", 50,"nokia")
#
# my_bot.introduce()          # Output: Hello! I am Terminator.
# print(f"Battery before: {my_bot.battery}")
#
# my_bot.charge()             # Runs the charge code
# print(f"Battery after: {my_bot.battery}")
#
#
#
#
# # 1. The Blueprint
# class Robot:
#     pass  # 'pass' tells Python to do nothing for now
#
# # 2. Creating Objects (Instances)
# robot_1 = Robot()
# robot_2 = Robot()
#
# # 3. Adding data manually (Not the best way, but it works)
# robot_1.name = "Wall-E"
# robot_2.name = "R2-D2"
#
# print(f"I am {robot_1.name}")
# print(f"I am {robot_2.name}")
#
#

class Robot:
    def __init__(self,name,battery):
        self.name=name
        self.battery=battery

    def intro(self):
        print(f"I am {self.name} bot")

class FightingRobot(Robot):
    def __init__(self,name,battery,weapon_type):
        super().__init__(name,battery)
        self.weapon_type=weapon_type

    def weapon(self):
        print(f"{self.name} bot is of {self.weapon_type} type")

sky_bot=FightingRobot("Test",80,"Fire")

sky_bot.weapon()
sky_bot.intro()


class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

class Library:
    def __init__(self):
        self.book=[]


    def add_book(self,book):
        self.book.append(book)
        print(f"{book.title} is added in library")

    def show_books(self):
        print("below is list of books")
        for b in self.book:
            print(b.title)

my_lib=Library()
b1=Book("A","a")
b2=Book("B","b")

my_lib.add_book(b1)
my_lib.add_book(b2)

my_lib.show_books()





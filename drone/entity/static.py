from drone.entity.entity_ import Entity


class Static(Entity):
    pass









# class Robot:
#     def __init__(self, sound, job):
#         self.sound = sound
#         self.job = job
#
#     def work(self):
#         print("Doing " + str(self.job))
#
#     def make_sound(self):
#         print(self.sound)
#
#
# class BoopeyBoi(Robot):
#     def __init__(self):
#         self.sound = "Boop!"
#         self.job = "Boopin'"
#
#
# class VerboseBoi(Robot):
#     def work(self):
#         print("Gonna do a job")
#         print(self.job)
#         print("I did the job!")
#
#
#
# class LoudBoi(Robot):
#     def __init__(self, sound, job):
#         loud_sound = str(sound).upper()
#         super().__init__(self, loud_sound, job)
#
#
# normal_lad = Robot("beeeep", "not screaming")
# loud_lad = LoudBoi("beeeep", "screaming")
#
#
#
#
# class Person:
#     def __init__(self, name, health):
#         self.name = name
#         self.max_health = health
#
#     def be_hurt(self, amt):
#         self.health -= amt
#
#
# class HasArmor(Person):
#     armor = 0  # Set it yourself somewhere else!
#
#     def be_hurt(self, amt):
#         self.health -= amt - self.armor
#
#
# class ToughBoi(HasArmor)
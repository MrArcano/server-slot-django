from django.db import models

# Create your models here.
class Slot:
    
    symbols = ['a', 'k', 'q', 'p-blond', 'p-brown', 'p-pink', 'bonus', 'wild', 'p-forest']

    @staticmethod
    def generate_slot_symbols():
        import random

        slot = []
        for i in range(5):
            new_array = []
            for j in range(3):
                rand_num = random.randint(1, 100)
                if rand_num <= 60:
                    index = random.randint(0, 2)  # 60% probability
                elif rand_num <= 90:
                    index = random.randint(3, 5)  # 30% probability
                elif rand_num <= 95:
                    index = 6  # 5% probability
                elif rand_num <= 98:
                    index = 7  # 3% probability
                else:
                    index = 8  # 2% probability

                new_array.append(Slot.symbols[index])

            slot.append(new_array)

        return slot



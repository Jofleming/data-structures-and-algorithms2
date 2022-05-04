from data_structures.queue import Queue



class AnimalShelter:
    
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()
        self.shelter_list = []

    def enqueue(self, animal):
        if isinstance(animal, Dog) == True:
            self.dog_queue.enqueue(animal)
            self.shelter_list.append('dog')
        if isinstance(animal, Cat) == True:
            self.cat_queue.enqueue(animal)
            self.shelter_list.append('cat')

    def dequeue(self, pref=None):
        if pref.lower() == 'none':
            pref = self.shelter_list[0]
        if pref == None:
            pref = self.shelter_list[0]
        if pref.lower() == 'dog' and self.dog_queue:
            self.shelter_list.remove('dog')
            return self.dog_queue.dequeue()
        if pref.lower() == 'cat' and self.cat_queue:
            self.shelter_list.remove('cat')
            return self.cat_queue.dequeue()
        else:
            return None

class Dog:
    pass


class Cat:
    pass

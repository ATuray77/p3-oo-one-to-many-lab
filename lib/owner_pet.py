class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet, must be instance of Pet class")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type") 
        self.name = name
        self._pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)


    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type") 
        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner, must be instance of Owner class")
        self._owner = owner

    def __str__(self):
        return self.name
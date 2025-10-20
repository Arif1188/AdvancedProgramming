import copy

class Chiken:
    __name = "Chiken"
    __params = {"Height": 20, "Weight": 50}
    
    
    def __init__(self, donor: "Chiken" = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(self.get_params())
            
    def get_name(self):
        return self.__name
    
    def get_params(self):
        return self.__params
    
    def set_name(self, name):
        self.__name = name
        
    def set_params(self, weight):
        self.__params['Weight'] = weight
        
    def clone(self):
        return Chiken(self)
        
    
chiken_1 = Chiken()
chiken_2 = chiken_1.clone()
print(chiken_1.get_name(), chiken_1.get_params(), chiken_2.get_name(), chiken_2.get_params())
chiken_2.set_name("Kostya")
chiken_2.set_params(70)
print(chiken_1.get_name(), chiken_1.get_params(), chiken_2.get_name(), chiken_2.get_params())
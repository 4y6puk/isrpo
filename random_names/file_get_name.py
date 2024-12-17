import random
from wrds_lib import _nouns_, _adjectives_

class FunRandomName():  
    def __init__(self): 
        self.__adjective = _adjectives_
        self.__essential = _nouns_

    def __get_random_adjective(self):
        return random.choice(self.__adjective)

    def __get_random__essential(self): 
        return random.choice(self.__essential)

    def get_name(self):
        adjective = self.__get_random_adjective()
        ssential = self.__get_random__essential()
        return f"{adjective} {ssential}"
    

fun_name_generator = FunRandomName()
print(fun_name_generator.get_name())
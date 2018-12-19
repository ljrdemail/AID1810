class Student:
    # def __init__(self, name, age, score):
    #     self.name = name
    #     self.age = age
    #     self.score = score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_score(self, score):
        self.__score = score

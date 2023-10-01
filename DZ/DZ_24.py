class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()

    #
    def print_info(self):
        print(f'{self.name} => {self.notebook.model()}, {self.notebook.system()}, {self.notebook.computer_memory()}')

    class Notebook:

        def model(self):
            return "HP"

        def system(self):
            return "i7"

        def computer_memory(self):
            return "16"


human = Student('Roman')
human_2 = Student('Vladimir')
human.print_info()
human_2.print_info()



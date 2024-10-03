class Person:
    def __init__(self, name="No Name", surname="No Surname"):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    def __str__(self):
        return f"Person: {self._name} {self._surname}"
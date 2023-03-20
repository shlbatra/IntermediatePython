from dataclasses import dataclass, field


@dataclass(
    order=True, frozen=True
)  # dataclass automatically defines the init and repr fn.
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # self.sort_index = self.age #if frozen then cannot do this update
        object.__setattr__(
            self, "sort_index", self.strength
        )  # so as alternate use __setattr__ method

    def __str__(self):
        return f"{self.name}, {self.job}, {self.age}"


person1 = Person("b", "y", 30)
person2 = Person("a", "x", 31)
person3 = Person("a", "x", 30)
# person1.strength = 30 #This will fail de to frozen
print(person1)
print(id(person2))
print(id(person3))
print(person2 > person3)

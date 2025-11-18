class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Pass:
    def __init__(self, sender, receiver, nr_of_times):
        # instanties
        self.sender = sender        # Player die de pass geeft
        self.receiver = receiver    # Player die de pass ontvangt
        self.nr_of_times = nr_of_times  # aantal keer dat deze pass voorkomt

    # methodes
    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender

    def get_end(self):
        return self.receiver

    def __eq__(self, other):
        # True als other ook een Pass is én
        # dezelfde sender en receiver heeft
        return (
            isinstance(other, Pass)
            and self.sender == other.sender
            and self.receiver == other.receiver
        )

    def __str__(self):
        # bv: "Pass from Eden Hazard to Moussa Dembele"
        return f"Pass from {self.sender} to {self.receiver}"



    # veronderstel dat de klasse Player al bestaat
p1 = Player("Eden Hazard")
p2 = Player("Moussa Dembele")
p3 = Player("Romelu Lukaku")

pas1 = Pass(p1, p2, 5)
pas2 = Pass(p1, p2, 3)
pas3 = Pass(p2, p3, 2)

print(pas1)                # test __str__
print(pas1 == pas2)        # True (zelfde sender/receiver)
print(pas1 == pas3)        # False
print(pas1.get_weight())   # 5

import csv


# ============================================================
# 1. NODE CLASS
# ============================================================
# Dit is de bouwsteen van de linked list: elke node bevat
# één taak + pointer naar de volgende node in de lijst.

class Node:
    def __init__(self, task_name, duration, priority):
        self.task_name = task_name  # naam van de taak
        self.duration = duration  # duur in minuten
        self.priority = priority  # 1 = hoogste prioriteit
        self.next = None  # volgende node (of None)


# ============================================================
# 2. LINKED LIST VOOR TAKEN
# ============================================================
# Bevat head, tail en alle methodes om taken te beheren.
# Lijkt op de LinkedList uit je cursus, maar aangepast voor tasks.

class TaskLinkedList:
    def __init__(self):
        self.head = None  # eerste node
        self.tail = None  # laatste node
        self.size = 0  # aantal nodes

    # --------------------------------------------------------
    # Voeg taak toe aan het einde van de lijst
    # --------------------------------------------------------
    def add_task(self, task_name, duration, priority):
        new_node = Node(task_name, duration, priority)

        # Als lijst leeg is → head = tail = nieuwe node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Tail.next wijst naar nieuwe node
            self.tail.next = new_node
            # Tail verschuift naar de nieuwe node
            self.tail = new_node

        self.size += 1

    # --------------------------------------------------------
    # Print alle taken op volgorde
    # --------------------------------------------------------
    def display_tasks(self):
        current = self.head
        while current is not None:
            print(f"Task: {current.task_name}, duration={current.duration}, priority={current.priority}")
            current = current.next

    # --------------------------------------------------------
    # Zoek een taak op naam
    # --------------------------------------------------------
    def find_task(self, task_name):
        current = self.head
        while current is not None:
            if current.task_name == task_name:
                return current
            current = current.next
        return None

    # --------------------------------------------------------
    # Verwijder taak (verwijderen van node in singly linked list)
    # --------------------------------------------------------
    def remove_task(self, task_name):
        current = self.head
        prev = None

        while current is not None:
            if current.task_name == task_name:

                # Case 1: huidige node is head
                if prev is None:
                    self.head = current.next

                    # Als lijst nu leeg is → tail = None
                    if current == self.tail:
                        self.tail = None

                # Case 2: node zit NIET in head
                else:
                    prev.next = current.next

                    # node was tail → tail opschuiven
                    if current == self.tail:
                        self.tail = prev

                self.size -= 1
                return True

            prev = current
            current = current.next

        return False  # niet gevonden

    # --------------------------------------------------------
    # Bereken totale duurtijd van alle taken
    # --------------------------------------------------------
    def calculate_total_duration(self):
        total = 0
        current = self.head

        while current is not None:
            total += current.duration
            current = current.next

        return total

    # --------------------------------------------------------
    # CSV inlezen, ziet er zo uit: task_name,duration,priority
    # --------------------------------------------------------
    def read_tasks_from_csv(self, file_path):
        file = open(file_path, "r")  # open het CSV-bestand in read-mode

        first_line = file.readline()  # lees header  (task_name,duration,priority)
#als we een header lezen dan gaat de cursor ook verder, dus we lezen die hierna niet nog eens
        for line in file:
            line = line.strip()  # newline wegdoen, strip() verwijdert alle spaties en speciale whitespace
# aan het begin én aan het einde van een string.
            if line == "":  # lege lijn overslaan
                continue

            parts = line.split(",")  # CSV opsplitsen in 3 delen
            task_name = parts[0]
            duration = int(parts[1])  # converteren naar int
            priority = int(parts[2])

            # voeg taak toe aan linked list
            self.add_task(task_name, duration, priority)

        file.close()  # bestand sluiten

    # --------------------------------------------------------
    # HELPER 1: sorted_insert_by_priority
    # Voegt één node in in een (al gesorteerde) linked list
    # waarbij we sorteren op duration (kortste taak eerst).
    #
    # head: begin van de NIEUWE (gesorteerde) lijst
    # node: de node die we willen invoegen
    #
    # Geeft de (mogelijk nieuwe) head van de lijst terug.
    # --------------------------------------------------------
    def sorted_insert_by_priority(self, head, node):
        # Case 1: lege lijst → node wordt eerste element
        if head is None:
            node.next = None
            return node

        # Case 2: node moet VOOR de huidige head komen
        # (duration kleiner dan die van head)
        if node.duration < head.duration:
            node.next = head
            return node

        # Case 3: zoek plaats ergens in het midden / einde
        current = head
        # zolang er een volgende is én die volgende duration <= node.duration
        while current.next is not None and current.next.duration <= node.duration:
            current = current.next

        # node invoegen na current
        node.next = current.next
        current.next = node

        return head

    # --------------------------------------------------------
    # HELPER 2: sorted_insert_by_priority_duration
    # Voegt één node in in een (al gesorteerde) linked list
    # op basis van:
    #   1) priority (lager getal = belangrijker)
    #   2) bij gelijke priority: duration (korter eerst)
    #
    # head: begin van de NIEUWE (gesorteerde) lijst
    # node: node die ingevoegd wordt
    #
    # Geeft de (mogelijk nieuwe) head van de lijst terug.
    # --------------------------------------------------------
    def sorted_insert_by_priority_duration(self, head, node):
        # Case 1: lege lijst
        if head is None:
            node.next = None
            return node

        # Bepaal of node VOOR head moet komen:
        # - lagere priority
        # - of zelfde priority maar kleinere duration
        if (node.priority < head.priority) or \
           (node.priority == head.priority and node.duration < head.duration):
            node.next = head
            return node

        # Anders zoeken we de juiste plek verder in de lijst
        current = head
        while current.next is not None:
            # node hoort vóór current.next als hij "beter" is:
            if (node.priority < current.next.priority) or \
               (node.priority == current.next.priority and node.duration < current.next.duration):
                break # als het zo is stoppen we de while loop

            current = current.next #als het niet zo is verschuiven we

        # node invoegen na current # stel A, B en we voegen C ertussen in
        node.next = current.next #de current next van A is momenteel B, maar C komt ertussen, de next van C zal dus B zijn
        current.next = node # de nieuwe current van A is C

        return head

    # --------------------------------------------------------
    # REORDER 1: reorder_tasks_by_priority
    #
    # Bouwt een NIEUWE gesorteerde lijst op, door elke node uit
    # de huidige lijst één voor één in te voegen op basis van
    # duration (kortste taak eerst) via sorted_insert_by_priority.
    #
    # Na afloop verwijst self.head naar de gesorteerde lijst.
    # --------------------------------------------------------
    def reorder_tasks_by_priority(self):
        new_head = None          # head van de nieuwe gesorteerde ketting
        current = self.head      # we beginnen bij de oude head

        # Loop over de oude lijst
        while current is not None:
            next_node = current.next   # onthoud waar de oude ketting verder gaat
            current.next = None        # maak de huidige node "los" uit de oude ketting, ze heeft geen next meer

            # voeg de node in in de nieuwe, gesorteerde ketting
            new_head = self.sorted_insert_by_priority(new_head, current)

            # ga verder in de oude lijst
            current = next_node

        # Koppel de nieuwe gesorteerde ketting terug aan dit object
        self.head = new_head

        # Tail opnieuw bepalen door naar het einde van de nieuwe lijst te lopen
        t = new_head
        if t is None:
            self.tail = None
        else:
            while t.next is not None:
                t = t.next
            self.tail = t

    # --------------------------------------------------------
    # REORDER 2: reorder_tasks_by_priority_duration
    #
    # Zelfde idee als hierboven, maar nu sorteren we:
    #   1) op priority (laagste getal eerst)
    #   2) bij gelijke priority op duration (kortste eerst)
    #
    # Dit gebruikt de helper sorted_insert_by_priority_duration.
    # --------------------------------------------------------
    def reorder_tasks_by_priority_duration(self):
        new_head = None
        current = self.head

        while current is not None:
            next_node = current.next   # oude link bewaren
            current.next = None        # node losmaken uit oude ketting

            # invoegen volgens priority → duration
            new_head = self.sorted_insert_by_priority_duration(new_head, current)

            current = next_node

        self.head = new_head

        # tail opnieuw bepalen
        t = new_head
        if t is None:
            self.tail = None
        else:
            while t.next is not None:
                t = t.next
            self.tail = t

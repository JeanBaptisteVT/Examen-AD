from typing import no_type_check_decorator


class Node:
    def __init__(self, task_name, duration, priority):
       self.task_name = task_name
       self.duration = duration
       self.priority = priority
       self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_task(self, task_name, duration, priority):
        new_node = Node(task_name, duration, priority)
        if self.tail is None:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.size += 1

    def remove_task(self, task_name):
        current = self.head
        prev = None

        while current is not None:
            if current.task_name == task_name:
                if prev is None:
                    self.head = current.next

                    if current == self.tail:
                        self.tail = None

                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev

                self.size -= 1
                return True
            prev = current
            current = current.next

        return False

    def display_tasks(self):
        current = self.head
        while current is not None:
            print(current.task_name)
            current = current.next

    def find_task(self, task_name):
        current = self.head
        while current is not None:
            if current.task_name == task_name:
                return current
            # of return (current.task_name, current.duration, current.priority)
            current = current.next

        return None

    def calculate_total_duration(self):
        current = self.head
        total_duration = 0
        while current is not None:
            total_duration += current.duration
            current = current.next

        return total_duration

    def read_tasks_from_csv(self, file_path):
        file = open(file_path, 'r')

        first_line = file.readline()

        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(',')
            task_name = parts[0]
            duration = int(parts[1])
            priority = int(parts[2])

            self.add_task(task_name, duration, priority)

        file.close()

# hier zetten we een node op de juiste plaats in een lijst die al gerangschikt is op priority
# we bouwen een nieuwe gesorteerde LL op via insertion (iedere keer afvragen, op welke plaats in de lijst zetten we ons nieuw element)
# LL heeft geen indexen, we zullen de nodes dus eruit halen, sorteren en een nieuwe lijst bouwen
    def sorted_insert_by_priority(self, task_name, priority):
        current = self.head
        list = []
        while current is not None:

#hier hetzelfde, maar node moet voor komen als priority kleiner is of priority gelijk en duration kleiner
    def sorted_insert_by_priority_duration(self, head, node):
        if head is None:
            node.next = None
            return node

#nu: hoe reorderen we een volledige lijst?
#dus we reorderen de hele lijst door iedere keer die sorted_ functie op te roepen voor iedere node,
#binnen onze reorder functie
    def reorder_tasks_by_priority(self):
        pass

    def reorder_tasks_by_priority_duration(self):
        pass






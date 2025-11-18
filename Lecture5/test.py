class Node:
    # iedere node bevat een element en een
    # pointer naar de volgende node
    # we gebruiken nodes omdat LL niet werken met indices zoals python lists
    # mylist[3] gaat dus niet
    def __init__(self, element):
        self.element = element
        self.next = None #none is als je de laatste bent


head = None #a variable that refers to the first node in the list
tail = None # a variable that refers to the last node in the list

head = Node("Chicago")
tail = head

tail.next = Node("Denver")

tail = tail.next #onze tail moet naar Denver verwijzen

tail.next = Node("Dallas")
tail = tail.next

current = head #we starten van de head node
while current != None:
    print(current.element)
    current = current.next


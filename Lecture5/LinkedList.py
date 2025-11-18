 # The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0 #gewoon dat we zien hoeveel elementen in onze lijst zitten

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0: #ben ik niet nul? anders heb ik geen first
            return None
        else:
            return self.__head.element #naar de head
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element #naar de tail

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the old head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size
# normaal moet tail niet aangepast worden, maar als we geen element in onze lijst hebben:
        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle #stel ABCD we willen X toevoegen op index 2 (waar C nu staat)
            current = self.__head #current is A
            for i in range(1, index):  #range 1, 2
                current = current.next # current = B
            temp = current.next #temp = C
            current.next = Node(e) # maak nieuwe node aan en nieuwe current.next van B wordt dus Node(e)
            (current.next).next = temp #de next van current.next (dus node(e)) wordt dus C
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element e
    def contains(self, e):
        current = self.__head  # start bij de eerste node
        while current is not None:  # loop door de hele lijst
            if current.element == e:  # element gevonden?
                return True  # ja → return True
            current = current.next  # anders verder naar de volgende node
        return False  # niet gevonden → False

    # Remove the element e and return true if it was removed
    def remove(self, e):
        current = self.__head  # start bij de head
        prev = None  # houdt de vorige node bij

        while current is not None:  # loop door de lijst
            if current.element == e:  # element gevonden?

                # Case 1: element zit in head
                if prev is None:
                    self.__head = current.next  # head verschuift 1 node vooruit

                    # Als het de enige node was, wordt tail ook None
                    if current == self.__tail:
                        self.__tail = None

                # Case 2: element zit NIET in head
                else:
                    prev.next = current.next  # sla de huidige node over

                    # Als de node de tail was, verschuift tail naar prev
                    if current == self.__tail:
                        self.__tail = prev

                self.__size -= 1  # lijst wordt kleiner
                return True  # verwijderen gelukt

            prev = current  # bewaar huidige als vorige
            current = current.next  # ga verder naar volgende node

        return False  # niet gevonden → niets verwijderen

    # Return the element at a given index
    def get(self, index):
        # index check
        if index < 0 or index >= self.__size:
            return None

        current = self.__head  # start bij de head

        # loop index aantal stappen
        for i in range(index):
            current = current.next

        return current.element  # return het element op positie index

    # Return the first index of element e, or -1 if not found
    def indexOf(self, e):
        current = self.__head  # start bij head
        index = 0  # huidige positie in de lijst

        while current is not None:
            if current.element == e:  # element gevonden?
                return index  # return positie
            current = current.next  # anders verder
            index += 1  # index verhogen

        return -1  # niet gevonden

    # Return the last index of element e, or -1 if not found
    def lastIndexOf(self, e):
        current = self.__head  # start bij head
        index = 0  # huidige index
        last_found = -1  # onthoud de laatste match

        while current is not None:
            if current.element == e:  # element gevonden?
                last_found = index  # update laatste positie
            current = current.next  # naar volgende node
            index += 1  # index verhogen

        return last_found  # -1 als nooit gevonden

    # Replace the element at given index with e, return old value
    def set(self, index, e):
        if index < 0 or index >= self.__size:  # index out of range
            return None

        current = self.__head  # start bij head

        for i in range(index):  # loop naar de node op index
            current = current.next

        old_value = current.element  # bewaar oude waarde
        current.element = e  # vervang door nieuwe waarde
        return old_value  # return oude element

    # Return elements via indexer
 #   def __getitem__(self, index):
  #      return self.get(index)


  # def __iter__(self):
       #  return LinkedListIterator(self.__head)'''


#'''class LinkedListIterator:
  #  def __init__(self, head):
  #      self.current = head
#
   # def __next__(self):
   #     if self.current == None:
   #         raise StopIteration
   #    else:
    #        element = self.current.element
    #        self.current = self.current.next
    #        return element   '''

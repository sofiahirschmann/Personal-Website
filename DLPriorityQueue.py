import DLNode


class DLPriorityQueue:

    def __init__(self):
       
        self._front = None
        self._rear = None
        self.length = 0

    def size(self):
        #returns an int representing the size of the SLPriorityQueue
        return(self.length)

    def is_empty(self):
        #returns True (if empty) or False
        return(self.length == 0)

    def enqueue(self,item):
        
        #create new node
        n = DLNode.DLNode(item)

        #if Queue is empty this node will be both front and rear
        if self.is_empty():
           
            self._front = n
            self._rear = n

        else:
            
            i = self._front

            #if the i is lesser priority to item...make item new front 
            if i.get_data() > item: 
                n.set_next(self._front)
                self._front.set_prev(n)
                self._front = n

            #if front is greater priority than item
            elif i.get_data() < item: 
                #if there is only one other node in queue you make this new node the rear
                if self.length == 1:
                    self._rear = n
                    self._front.set_next(n)
                    n.set_prev(self._front)

                else:
                    
                    #while i is not the rear and does not == None
                    while i != self._rear and i != None: 

                        #see what comes next
                        temp = i.get_next()

                        #if that next node is lesser priority to item
                        if temp.get_data() > item:

                            #items next node is i's next node
                            n.set_next(temp)
                            temp.set_prev(n)

                            #i's new next node become item
                            i.set_next(n)
                            n.set_prev(i)

                            #i is now none so loop ends
                            i = None

                        elif temp.get_data() == item:

                            #items next node is i's next node
                            n.set_next(temp)
                            temp.set_prev(n)

                            #i's new next node become item
                            i.set_next(n)
                            n.set_prev(i)

                            #i is now none so loop ends
                            i = None
                    
                        else:
                            #keep getting next to figure out priority until you get to rear
                            i = i.get_next()
                
                    #if i ends up reaching self._rear
                    if i == self._rear:

                        #if that is the case the new rear become item and that item becomes the rear's next
                        self._rear.set_next(n)
                        n.set_prev(self._rear)
                        self._rear = n

            

        self.length += 1

    def dequeue(self):

        #returns and removes the _front of the queue
        if self.is_empty():
            return None
        
        #store front node in data
        data = self._front.get_data()

        #new front is the next of old front and remove what was previous to node
        self._front = self._front.get_next()
        
        if self._front != None:
            self._front.rem_prev()

        #subtract one from length
        self.length -= 1

        #if the Queue is now empty make front and rear none
        if (self.length == 0 ):
            self._front = None
            self._rear = None

        #return what was removed from Queue
        return(data)

    def first(self):

        if self.is_empty():
            return None
        return(self._front.get_data())


    def reverse(self):

        #start off s as empty
        s = ""

        #if the Queue is empty you're just returning an empty s
        if self.is_empty():
            return s 
        
        #otherwise start next as rear and add it to s
        next = self._rear
        
        s += str(next)
        next = next.get_prev()

        #if there is more than one node... add commas in between nodes added
        while next != None:
            s += ", " + str(next.get_data())
            next = next.get_prev()
        return s


    def __str__(self):
        
        #start off s as empty
        s = "List contents: "

        #if the Queue is empty you're just returning an empty s
        if self.is_empty():
            return s 
        
        #otherwise start next as front and add it to s
        next = self._front
        
        s += str(next)
        next = next.get_next()

        #if there is more than one node... add commas in between nodes added
        while next != None:
            s += ", " + str(next)
            next = next.get_next()
        return s
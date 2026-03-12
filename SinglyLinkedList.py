class ListElement:
    def __init__(self, data):
        self.data = data
        self.next_node = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = ListElement("Sentinel_Header")

    def __iter__(self):
        current = self.head.next_node
        while current:
            yield current.data
            current = current.next_node

    def add_last(self, value):
        new_node = ListElement(value)
        last = self.get_last_node()
        last.next_node = new_node

    def insert_after(self, prev_item, new_item):
        current = self.head.next_node
        while current and current.data != prev_item:
            current = current.next_node
        
        if current:
            new_node = ListElement(new_item)
            new_node.next_node = current.next_node
            current.next_node = new_node

    def delete(self, value):
        current = self.head
        while current.next_node:
            if current.next_node.data == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def find(self, value):
        current = self.head.next_node
        while current:
            if current.data == value:
                return True
            current = current.next_node
        return False

    def get_first_node(self):
        return self.head.next_node

    def get_last_node(self):
        current = self.head
        while current.next_node:
            current = current.next_node
        return current

    def write_list(self):
        output = [str(data) for data in self]
        if not output:
            print("Liste ist leer")
            return
        print(" -> ".join(output))

if __name__ == "__main__":
    my_list = SinglyLinkedList()
    my_list.add_last("1")
    my_list.add_last("2")
    my_list.add_last("3")
    
    for item in my_list:
        print(item)
    
    my_list.write_list()

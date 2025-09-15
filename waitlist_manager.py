class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        """Add a customer to the front of the waitlist."""
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        """Add a customer to the end of the waitlist."""
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        """Remove a customer by name from the waitlist."""
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return f"Removed {name} from the waitlist"
            previous = current
            current = current.next
        return f"{name} not found"

    def print_list(self):
        """Print all customers currently in the waitlist."""
        if not self.head:
            print("The waitlist is empty")
            return
        print("Current waitlist:")
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    waitlist = LinkedList()
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            print(waitlist.add_end(name))
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name))
        elif choice == "4":
            waitlist.print_list()
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    waitlist_generator()
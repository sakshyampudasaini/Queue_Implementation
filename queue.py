# queue.py

queue = []

while True:
    choice = int(input('''
        1. Enqueue (Add Element)
        2. Dequeue (Remove First Element)
        3. Front Element
        4. Rear Element
        5. Display Queue
        6. Exit
        
        Enter your choice:-- 
    '''))

    if choice == 1:
        value = input("Enter the value:-- ")
        queue.append(value)
        print("Queue:", queue)

    elif choice == 2:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            removed = queue.pop(0)
            print(f"Removed element: {removed}")
            print("Queue:", queue)

    elif choice == 3:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            print("Front Queue Value:", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            print("Rear Queue Value:", queue[-1])

    elif choice == 5:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            print("Queue:", queue)

    elif choice == 6:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

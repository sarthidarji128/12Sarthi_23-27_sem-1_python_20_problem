class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek an empty stack.")

    def size(self):
        return len(self.items)


testStack = Stack()

testStack.push(10)
testStack.push(30)
testStack.push(50)

peekEle = testStack.peek()
print(f"Top element: {peekEle}")

popEle = testStack.pop()
print(f"Popped element: {popEle}")

print(f"Is the stack empty? {testStack.isEmpty()}")

size = testStack.size()
print(f"Size of the stack: {size}")

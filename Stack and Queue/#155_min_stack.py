'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        

    def push(self, val: int) -> None:
        currMin = self.getMin()
        if currMin == None or currMin > val:
            currMin = val
        self.st.append((val, currMin))
        print(self.st)
        

    def pop(self) -> None:
        self.st.pop()
        print(self.st)
        

    def top(self) -> int:
        return self.st[-1][0] if self.st else None
        
    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None




        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.pop()

param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
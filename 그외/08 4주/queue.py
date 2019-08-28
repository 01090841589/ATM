def enQueue(item):
    global rear
    if isFull() :
        print("Queue_Full")
    else:
        rear += 1
        Q[rear] = item


def deQueue():
    global front
    if isEmpty():
        return
    else:
        front += 1
        return Q[front]


def isFull():
    return rear == len(Q)-1


def isEmpty():
    global front, rear
    return front == rear


def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return Q[front+1]


SIZE = 4
Q = [0]*SIZE
front, rear = -1, -1

enQueue(1)
enQueue(2)
enQueue(3)
print(Q)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(front, rear)
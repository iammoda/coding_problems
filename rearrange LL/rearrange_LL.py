def rearrangeLinkedList(head, k):
    smallerHead = None
    smallerTail = None
    equalHead = None
    equalTail = None
    largerHead = None
    largerTail = None

    node = head
    while node is not None:
        if node.value < k:
            smallerHead, smallerTail = growLL(smallerHead, smallerTail, node)
        elif node.value > k:
            largerHead, largerTail = growLL(largerHead, largerTail, node)
        else:
            equalHead, equalTail = growLL(equalHead, equalTail, node)

        prevNode = node
        node = node.next
        prevNode.next = None

    firstHead, firstTail = joinLL(smallerHead, smallerTail, equalHead, equalTail)
    finalHead, _ = joinLL(firstHead, firstTail, largerHead, largerTail)

    return finalHead


def growLL(head, tail, node):
    newHead = head
    newTail = node

    if newHead is None:
        newHead = node
    if tail is not None:
        tail.next = node

    return (newHead, newTail)


def joinLL(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:
        tailOne.next = headTwo

    return (newHead, newTail)


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


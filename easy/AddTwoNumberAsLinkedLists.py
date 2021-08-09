from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_two_lists(first, second):
    num_1 = ''
    num_2 = ''
    while first:
        if first.data == -1:
            break
        num_1 += str(first.data)
        first = first.next
    while second:
        if second.data == -1:
            break
        num_2 += str(second.data)
        second = second.next

    tmp_list = list(map(int, str(int(num_1) + int(num_2)))) + [-1]
    head = Node(tmp_list[0])
    last = head
    for data in tmp_list[1:]:
        if data == -1:
            break
        last.next = Node(data)
        last = last.next
    return head


# Taking input.
def take_input(m_input_list):
    first_list = None
    second_list = None

    arr = m_input_list[0]
    if arr[0] != -1:
        first_list = Node(arr[0])
        last = first_list
        for data in arr[1:]:
            if data == -1:
                break
            last.next = Node(data)
            last = last.next

    arr = m_input_list[1]
    if arr[0] != -1:
        second_list = Node(arr[0])
        last = second_list
        for data in arr[1:]:
            if data == -1:
                break
            last.next = Node(data)
            last = last.next

    return first_list, second_list


# Function to print the node values of the linked list.
def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print(-1)


if __name__ == "__main__":
    inputs = ([[1, 2, -1], [3, 4, 5, -1]], [[2, 4, -1], [5, 3, -1]])
    for input_list in inputs:
        m_first, m_second = take_input(input_list)
        answerList = add_two_lists(m_first, m_second)
        print_linked_list(answerList)

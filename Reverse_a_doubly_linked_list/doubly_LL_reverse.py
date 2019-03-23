#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

def reverse(head):

    temp = None
    while head.next:
        head = head.next
    H = head
    while head:
        temp = head.next
        head.next = head.prev
        head.prev = temp
        head = head.next

    return H


if __name__ == '__main__':

    t = [1,2,3,4]
    llist = DoublyLinkedList()
    for i in t:
        llist.insert_node(i)

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1)


from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

import pandas
from array import *

import os

#This is the Sorting section below

def LoadData():

    #this is where we do the intial loading of the csv file into to show the data format in the file 
    #which has not been sorted at all

    newArray = []
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Name.csv')
    array=pandas.read_csv(filename)
    array=array.values.tolist()
    
    return sortcolumn(array)

# This function compare two strings and return TRUE if string A is bigger, FALSE if it is lower or equal.        
def isStringBigger(A,B):
    lenA=len(A)
    lenB=len(B)
    maxlen=max(lenA,lenB)
    
    if lenA==0 and lenB==0:
        return False
    elif lenA==0:
        return False
    elif lenB==0:
        return True
    
    for i in range (0,maxlen):
        if ord(A[i].upper())>ord(B[i].upper()):
            return True
        elif ord(A[i].upper())<ord(B[i].upper()):
            return False
    
    if lenA>lenB:
        return True
    else:
        return False

# This function uses insertion sort to sort a list alphabetically using as a reference the first element inside the tuples (the name)
def InsertionSortalphabetical(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and isStringBigger(array[j - 1][0], temp[0]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp      
    return array

# This function uses merge sort to sort a list alphabetically using as a reference the first element inside the tuples (the name)
def MergeSortalphabetical(array):
    if len(array)>1:
        middle = len(array)//2
        leftside = array[:middle]
        rightside = array[middle:]
        MergeSortalphabetical(leftside)
        MergeSortalphabetical(rightside)
        i=0
        j=0
        k=0
        while i < len(leftside) and j < len(rightside):
            if isStringBigger(rightside[j][0],leftside[i][0]):
                array[k]=leftside[i]
                i=i+1
            else:
                array[k]=rightside[j]
                j=j+1
            k=k+1

        while i < len(leftside):
            array[k]=leftside[i]
            i=i+1
            k=k+1

        while j < len(rightside):
            array[k]=rightside[j]
            j=j+1
            k=k+1
    return array

# This function uses insertion to sort a list by number of points using as a reference the second element inside the tuples
def InsertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and array[j - 1][1] > temp[1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp      
    return array

# This function uses merge sort to sort a list by number of points using as a reference the second element inside the tuples
def MergeSort(array):
    if len(array)>1:
        middle = len(array)//2
        leftside = array[:middle]
        rightside = array[middle:]
        MergeSort(leftside)
        MergeSort(rightside)
        i=0
        j=0
        k=0
        while i < len(leftside) and j < len(rightside):
            if leftside[i][1] < rightside[j][1]:
                array[k]=leftside[i]
                i=i+1
            else:
                array[k]=rightside[j]
                j=j+1
            k=k+1

        while i < len(leftside):
            array[k]=leftside[i]
            i=i+1
            k=k+1

        while j < len(rightside):
            array[k]=rightside[j]
            j=j+1
            k=k+1
    return array

# This function separate the client into three types of users: Silver Gold and Platinum and order them based on the previous sorting approach used (by points or by name)
def sortcolumn(namelist):

    newArraySilver = []
    newArrayGold = []
    newArrayPlatinum = []

    averageclient = 0
    maxclient = 0

    for i in range(len(namelist)):

        averageclient = averageclient + namelist[i][1] / len(namelist)

        if maxclient < namelist[i][1]:
            maxclient = namelist[i][1]
            
        if namelist[i][1] > 5000:
            first_name, last_name = namelist[i][0].split(" ")
            newArrayPlatinum.append({'firstname': first_name, 'lastname': last_name, 'points': namelist[i][1]})
        if namelist[i][1] > 1000:
            first_name, last_name = namelist[i][0].split(" ")
            newArraySilver.append({'firstname': first_name, 'lastname': last_name, 'points': namelist[i][1]})
        else:
            first_name, last_name = namelist[i][0].split(" ")
            newArrayGold.append({'firstname': first_name, 'lastname': last_name, 'points': namelist[i][1]})

        newObject = []
        newObject.append({'newArrayGold': newArrayGold, 'newArraySilver': newArraySilver, 'newArrayPlatinum': newArrayPlatinum, 'averageclient': averageclient, 'maxclient': maxclient})
          
    return newObject

# This function select the optimal alphabetical sorting method based on the size of the list              
def click_SortDBalpha():

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Name.csv')
    namelist = pandas.read_csv(filename, header=None)

    if len(namelist)<100:
        namelist=pandas.DataFrame(InsertionSortalphabetical(namelist.values.tolist()))
        namelist=namelist.values.tolist()
    else:
        namelist=pandas.DataFrame(MergeSortalphabetical(namelist.values.tolist()))
        namelist=namelist.values.tolist()
    
    return sortcolumn(namelist)

# This function select the optimal numerical sorting method based on the size of the list               
def click_SortDBpoint():
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Name.csv')
    namelist = pandas.read_csv(filename, header=None)

    if len(namelist)<100:
        namelist=pandas.DataFrame(InsertionSort(namelist.values.tolist()))
        namelist=namelist.values.tolist()
    else:
        namelist=pandas.DataFrame(MergeSort(namelist.values.tolist()))            
        namelist=namelist.values.tolist()

    return sortcolumn(namelist)
########################################

#This is the hash-based search section below
class Node:
    def __init__(self, data=None):
        # Initialise Node
        self.data = data
        self.next = None


class Customers:
    def __init__(self):
        # Initialise the Customers singly linked list
        self.head = Node()

    def append(self, data):
        # Appends a node to the end of the Customers singly linked list
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            if current.next.data.first_name == new_node.data.first_name and current.next.data.last_name == new_node.data.last_name:
                current.next.data.occurrences += 1
                new_node.data.occurrences += 1
            current = current.next
        current.next = new_node

    def find(self, first_name, last_name):
        # Find and retrieve customer occurrences matching the first and last name
        occurrences = 0
        customers = []
        current_node = self.head
        while current_node.next is not None and occurrences < current_node.next.data.occurrences:
            current_node = current_node.next
            if current_node.data.first_name == first_name and current_node.data.last_name == last_name:
                customers.append(current_node.data)
                occurrences += 1
        return customers


class Customer:
    def __init__(self, first_name, last_name, loyalty_points):
        # Initialise Customer
        self._first_name = first_name
        self._last_name = last_name
        self._occurrences = 1
        self._loyalty_points = loyalty_points

    def __str__(self):
        # String representations of the Customer object
        return "{} {} {}".format(self.first_name, self.last_name, self.loyalty_points)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def occurrences(self):
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        self._occurrences = occurrences

    @property
    def loyalty_points(self):
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, loyalty_points):
        self._loyalty_points = loyalty_points


class HashBasedSearch:
    def __init__(self, elements_to_add=None):
        # Initialise the hash table and populate data structures
        initial_size = len(elements_to_add)
        if self.is_prime(initial_size):
            self.array_size = initial_size
        else:
            self.array_size = self.get_next_prime(initial_size)

        self.hash_table = []
        for i in range(self.array_size):
            self.hash_table.append(Customers())
        self.load_hash_table(elements_to_add)

    def hash_code(self, first_name, last_name):
        # Produce hash code based on supplied first and last name
        customer_to_hash = first_name.lower() + last_name.lower()
        hash_key_value = 0
        for ch in customer_to_hash:
            # The character code for 'a' is 97 so subtract so that character code start at 1
            character_code = ord(ch) - 96
            # Using 26 letters plus blank to calculate the hash key
            hash_key_value = (hash_key_value * 27 + character_code) % self.array_size
        return hash_key_value

    def load_hash_table(self, elements_to_add):
        # Load the hash table with created Customer
        for i in range(len(elements_to_add)):
            first_name = elements_to_add[i]['firstname']
            last_name = elements_to_add[i]['lastname']
            loyalty_point = elements_to_add[i]['points']
            new_customer = Customer(first_name, last_name, loyalty_point)
            self.append(new_customer)

    def get_next_prime(self, min_number_to_check):
        # Get the next prime number after minimum number to check
        i = min_number_to_check
        while not self.is_prime(i):
            i += 1
        return i

    @staticmethod
    def is_prime(number):
        # Determine if number is prime
        if number == 2 or number == 3:
            return True
        if number < 2 or number % 2 == 0:
            return False
        if number < 9:
            return True
        if number % 3 == 0:
            return False
        root = int(number ** 0.5)
        factor = 5
        while factor <= root:
            if number % factor == 0:
                return False
            if number % (factor + 2) == 0:
                return False
            factor += 6
        return True

    def append(self, new_customer):
        # Generate hash key and append the Customer in the linked list specified by the hash key
        hash_key = self.hash_code(new_customer.first_name, new_customer.last_name)
        self.hash_table[hash_key].append(new_customer)

    def find(self, first_name, last_name):
        # Find and retrieve customer occurrences matching the first and last name at location identified by the hash key
        hash_key = self.hash_code(first_name, last_name)
        customers = self.hash_table[hash_key].find(first_name, last_name)
        return customers


def main(searchValue):
            
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Name.csv')
    namelist = pandas.read_csv(filename, header=None)
    namelist = namelist.values.tolist()

    elements_to_add = []
    for i in range(len(namelist)):
        first_name, last_name = namelist[i][0].split(" ")
        elements_to_add.append({'firstname': first_name, 'lastname': last_name, 'points': namelist[i][1]})
    
    customer_hash_table = HashBasedSearch(elements_to_add)
    customer_look_up = searchValue
    first_name, last_name = customer_look_up.split(" ")

    found = [] 

    found_customers = customer_hash_table.find(first_name, last_name)
    for foundCustomer in found_customers:
        print(foundCustomer)
        found.append(foundCustomer)

    return found  
  ########################################



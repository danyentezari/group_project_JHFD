from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

import pandas
from array import *
import django_tables2 as tables

def LoadData():
    
    newArray = []
    lename="C:/Users/jeremye/Name.csv"
    array=pandas.read_csv(lename)
    array=array.values.tolist()
    
    for i in range(len(array)):
       first_name, last_name = array[i][0].split(" ")
       newArray.append({'firstname': first_name, 'lastname': last_name, 'points': array[i][1]})
    
    return newArray
    
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

def InsertionSortalphabetical(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and isStringBigger(array[j - 1][0], temp[0]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp      
    return array


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

def InsertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and array[j - 1][1] > temp[1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp      
    return array


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

def sortcolumn(self):

    countsilver=0
    countgold=0
    countplatinum=0

    # for i in range(0,len(self.namelist)):
    #     self.Qtable.setItem(i,0,QTableWidgetItem(str(self.namelist.iloc[i,0])))
    #     self.Qtable.setItem(i,1,QTableWidgetItem(str(self.namelist.iloc[i,1])))

    #     if self.namelist.iloc[i,1] > 5000:
    #         self.Qtable4.setItem(countplatinum,0,QTableWidgetItem(str(self.namelist.iloc[i,0])))
    #         self.Qtable4.setItem(countplatinum,1,QTableWidgetItem(str(self.namelist.iloc[i,1])))                
    #         countplatinum=countplatinum+1
    #     elif self.namelist.iloc[i,1] > 1000:
    #         self.Qtable3.setItem(countgold,0,QTableWidgetItem(str(self.namelist.iloc[i,0])))
    #         self.Qtable3.setItem(countgold,1,QTableWidgetItem(str(self.namelist.iloc[i,1])))                
    #         countgold=countgold+1
    #     else:
    #         self.Qtable2.setItem(countsilver,0,QTableWidgetItem(str(self.namelist.iloc[i,0])))
    #         self.Qtable2.setItem(countsilver,1,QTableWidgetItem(str(self.namelist.iloc[i,1])))                
    #         countsilver=countsilver+1
            
def click_SortDBalpha():

    newArray = []
    lename="C:/Users/jeremye/Name.csv"
    array=pandas.read_csv(lename)
    array=array.values.tolist()
    namelist = pandas.read_csv(lename, header=None)

    if len(namelist)<100:
        namelist=pandas.DataFrame(InsertionSortalphabetical(namelist.values.tolist()))
        namelist=namelist.values.tolist()
    else:
        namelist=pandas.DataFrame(MergeSortalphabetical(namelist.values.tolist()))
        namelist=namelist.values.tolist()
    
    #self.sortcolumn()

    print(namelist)

    for i in range(len(namelist)):
       first_name, last_name = namelist[i][0].split(" ")
       newArray.append({'firstname': first_name, 'lastname': last_name, 'points': namelist[i][1]})
    
    return newArray
            
def click_SortDBpoint():

    newArray = []
    lename="C:/Users/jeremye/Name.csv"
    array=pandas.read_csv(lename)
    array=array.values.tolist()
    namelist = pandas.read_csv(lename, header=None)

    if len(namelist)<100:
        namelist=pandas.DataFrame(InsertionSort(namelist.values.tolist()))
        namelist=namelist.values.tolist()
    else:
        namelist=pandas.DataFrame(MergeSort(namelist.values.tolist()))            
        namelist=namelist.values.tolist()

    #self.sortcolumn()

    print(namelist)

    for i in range(len(namelist)):
       first_name, last_name = namelist[i][0].split(" ")
       newArray.append({'firstname': first_name, 'lastname': last_name, 'points': namelist[i][1]})
    
    return newArray

#this is the search section below
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Customers:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        # Appends a node to the end
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            if current.next.data.first_name == new_node.data.first_name and current.next.data.last_name == new_node.data.last_name:
                current.next.data.count += 1
                new_node.data.count += 1
            current = current.next
        current.next = new_node

    def length(self):
        # Return the length of the list
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def search(self, first_name, last_name):
        # Returns all customers matching the specified data
        count = 0
        customers = []
        current_node = self.head
        while current_node.next is not None and count < current_node.next.data.count:
            current_node = current_node.next
            if current_node.data.first_name == first_name and current_node.data.last_name == last_name:
                customers.append(current_node.data)
                count += 1
        return customers

    def display(self):
        # displays each member of the list
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)


class Customer:

    def __init__(self, first_name, last_name, loyalty_points):
        self._first_name = first_name
        self._last_name = last_name
        self._count = 1
        self._loyalty_points = loyalty_points

    def __str__(self):
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
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @property
    def loyalty_points(self):
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, loyalty_points):
        self._loyalty_points = loyalty_points


class HashBasedSearch:

    def __init__(self, elements_to_add=None):
        # initialise the hash based and populate data structures
        self.array_size = len(elements_to_add)
        self.hash_table = []
        for i in range(self.array_size):
            self.hash_table.append(Customers())
        self.load_hash_table(elements_to_add)

    def hash_code(self, first_name, last_name):
        customer_to_hash = first_name.lower() + last_name.lower()
        hash_key_value = 0
        for ch in customer_to_hash:
            # 'a' has the character code of 97 so subtract
            # to make our letters start at 1
            character_code = ord(ch) - 96
            temp_hash_key_value = hash_key_value
            # Calculate the hash key using the 26 letters plus blank
            hash_key_value = (hash_key_value * 27 + character_code) % self.array_size
            # print("\n\t\t\t\t" + customer_to_hash + " Hash Key Value " + str(temp_hash_key_value) + " * 27 + Character Code " + str(character_code) + " % array_size " + str(self.array_size) + " = " + str(hash_key_value))
        return hash_key_value

    def load_hash_table(self, elements_to_add):
        # create and insert each customer into the ...
        for i in range(len(elements_to_add)):
            first_name = elements_to_add[i][0]
            last_name = elements_to_add[i][1]
            loyalty_point = elements_to_add[i][2]
            new_customer = Customer(first_name, last_name, loyalty_point)
            self.append(new_customer)

    def append(self, new_customer):
        # Generate hash key and append the customer in the linked list specified by the hash key
        hash_key = self.hash_code(new_customer.first_name, new_customer.last_name)
        self.hash_table[hash_key].append(new_customer)

    def search(self, first_name, last_name):
        # Retrieve all occurences of customer which matching the specified first name and last name
        hash_key = self.hash_code(first_name, last_name)
        customers = self.hash_table[hash_key].search(first_name, last_name)
        return customers

    def display(self):
        for i in range(self.array_size):
            print("Hash Table Index", i)
            self.hash_table[i].display()


def main(searchValue):
    elements_to_add = [
            ["Bruce", "Armstrong", "2800"],
            ["Doreen", "Bailey" , "50"],
            ["Michael", "Barker" , "200"],
            ["Anna", "Brown" , "32800"],
            ["Peter", "Cook" , "2320"],
            ["Paula", "Dixon" , "2500"],
            ["Babara", "Hamilton" , "100"],
            ["Claudia", "Hill" , "200"],
            ["Maureen", "Holmes" , "300"],
            ["Paul", "Jenkins" , "600"],
            ["Vanessa", "Johnson" , "60"],
            ["James", "Jones" , "700"],
            ["Patrick", "Lawrence" , "2800"],
            ["Adrian", "Lewis" , "5800"],
            ["Nanny", "Morris" , "1000"],
            ["Graham", "Reid" , "28"],
            ["Ava", "Richardson" , "430"],
            ["Hariet", "Robertson" , "2800"],
            ["Anne", "Taylor" , "6800"],
            ["Karen", "Turner" , "7800"],
            ["Mark", "Palmer" , "200"],
            ["Sharon", "Poole" , "900"],
            ["Tony", "Singh" , "1800"],
            ["Mary", "Smith" , "5800"],
            ["Sheila", "Spencer" , "200"],
            ["Kyle", "Stone" , "20"],
            ["Dawn", "Watson" , "40"],
            ["Fred", "Wilkinson" , "800"],
            ["Jim", "Williams" , "1000"],
            ["Jim", "Williams", "70"],
            ["Paulie", "Malignaggi", "3250"]]

    print("jeremy")
    customer_hash_table = HashBasedSearch(elements_to_add)
    customer_look_up = searchValue
    first_name, last_name = customer_look_up.split(" ")

    newDic = dict()
    found = [] 

    found_customers = customer_hash_table.search(first_name, last_name)
    for foundCustomer in found_customers:
        print(foundCustomer)
        found.append(foundCustomer)
    
    return found
  



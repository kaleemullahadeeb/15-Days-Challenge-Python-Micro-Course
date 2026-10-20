 #Learning datatypes in python
 #7 datatypes

#1. Text Datatype
#string 
customer_name = "Kaleem"
print ("customer name is:", customer_name)
print ("customer datatype is:", type(customer_name))

#Numeric datatype
#integer

rating = 5
quantity = 10
#for example
print ("rating of salesman:", type (rating))
print ("sales quantity:", type(quantity))

#Float
order_amount = 55400.50
print ("order_amount datatype is : ", type(order_amount))

#3 complex numbers
a=7+6j
print("data type of complex number (a): ", type(a))

#second example of complex number/same thing
a=5+6j
print (type(a))

# Boolean
is_paid = True
print ("is_paid:", type(True))

#Sequence
list
cities = ["Talagang", "Chakwal", "Rawalpindi", "Islamabad"]
print (cities)
print (type(cities))

#Tuple
dimension = (1080, 1920)
print (dimension)
print (type(dimension))

#Range
num=range (1,150)
print(list(num))
print(type(num))

num= range (100,111)
print (list (num))
print (type(num))

##Dictionary dict

employee = {
    "name":"Usman Aziz",
    "age": 23,
    "qualification" : "MSc"
}
print (employee)
print (type(employee))

student={
    "name": "Kaleem",
    "age": 21,
    "department": "Computer Science"
}
print (student)
print (type(student))

### set datatype
numbers={1,2,3,4,5,6}
print (numbers)
print (type(numbers))

#None datatype
remarks = None
print("remarks:", type(remarks))
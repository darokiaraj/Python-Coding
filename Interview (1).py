#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Write a program that prints the numbers from 1 to N. 
But, for multiples of three,  print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.


# In[18]:


N = int (input("Input: N= "))
for i in range (1, N):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)


# In[ ]:


# 2.  Given an array print all the numbers that are repeating in it and the number of times they are repeating.


# In[7]:


A = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1];
B = [None] * len(A);    
visited = -1;
   
for i in range(0, len(A)):    
    count = 1;    
    for j in range(i+1, len(A)):    
        if(A[i] == A[j]):    
            count = count + 1;    
            B[j] = visited;    
               
    if(B[i] != visited):    
        B[i] = count;
            
for i in range(0, len(B)):    
    if(B[i] != visited):
       print(str(A[i]) + " - " + str(B[i]));


# In[29]:


# 3. Given an object/dictionary, containing names as keys and amount_paid by each of them as values, 
write a function that takes such an object as input and calculates the total sum paid by them together.


# In[1]:


def returnSum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  
dict = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35} 
print("Sum :", returnSum(dict))


# In[ ]:


#4. Develop a program to calculate the total and individual player scores in a cricket match. 
Input would be an array with the index representing the ball number and the value representing the runs scored of that ball.


# In[ ]:





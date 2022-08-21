#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')

Ans) True and False are two values of the boolean data types.If a statement is said to be correct/true/right it shows True else the statement will be False. 
     True and False must start with an uppercase and the rest of the words in lowercase. 


# In[2]:


a=True 
b=False 

print(a,type(a))
print(b,type(b))


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans)The three differnt types of Boolean operators in python are: or, and ,not


# In[3]:


a=350
b=230
# Example of boolean and:
print(a>200 and b>219)
print(a>450 and b>200) #even if one statement is false the whole statement is false (b is false so whole statement is False)

# Example of boolean or
print(a>200 or b>100)
print(a>300 or b>500) #even if one statement is correct even though the other is wrong the statement in whole is True (even though b is wrong since a is correct the whole staement is True)
print(a>2000 or b>4000) #if both statements are wrong then the whole statement is False


# Example of boolean not
print(not(a>1000))
print(not(a>50))


# In[ ]:


3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).


Ans)The Truth tables for the boolean tables are as follows:

Truth Table for and operaotor
True and True is True
True and False is False
False and True is False
False and False is False

Truth Table for or operaotor
True and True is True
True and False is True
False and True is True
False and False is False

Truth Table for not operaotor
True not is False False not is True


# In[ ]:


4. 
get_ipython().set_next_input('What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)


# In[ ]:


#Ans)
print((5>4)and(3==5)) # False
print(not(5>4)) # False
print((5>4)or(3==5)) # True
print(not((5>4)or(3==5))) # False
print((True and True)and(True==False)) # False
print((not False)or(not True)) # True


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans) The Six comparision operators available in python are:
            == , != , < , > , <= , =>


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one. 

Ans) == is the equal to operator that compares two values and evaluates to a Boolean, while = is that assignment operator that stores a value in a variable.


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans) In Python, code block refers to a collection of code that is in the same block or indent. This is most commonly found in classes, functions, and loops.


# In[ ]:


spam = 0  
if spam == 10:  
    print('eggs')  # block 1
if spam > 5:  
    print('bacon')  # block 2
else:  
    print('ham')  # block 3
print('spam')  
print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# In[4]:


# 8 answer
spam=int(input())
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')


# In[5]:


spam=int(input())
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')


# In[6]:


spam=int(input())
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans)Press Ctrl-c to stop a program stuck in an infinite loop


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans)The break statement will move the execution outside the loop if break condtion is satisfied. Whereas the continue statement will move the execution to the start of the loop.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans)The Differences are as follows:

The range(10) call range from 0 to 9 (but not include 10)
The range (0,10) explicitly tells the loop to start at 0
The range(0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[7]:


# 12 Answer
print('-'*10,'Using For Loop','-'*10)
for i in range(1,11):
    print(i, end=" ")
print('\n')
print('-'*10,'Using While Loop','-'*10) 
i=1
while i<=10:
    print(i, end=" ")
    i+=1


# In[ ]:


13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Ans)This function can be called with spam.bacon()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





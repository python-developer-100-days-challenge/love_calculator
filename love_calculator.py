#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Love Calculator Script
# This script calculates a love score based on inputted names.

# Welcome message
print("Welcome to the Love Calculator!")

# Input names and convert to lowercase
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

# Calculate the occurrence counts for 'true' and 'love' in name1

#true1_count = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
#love1_count = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")

count1 = name1.count("t")
count2 = name1.count("r")
count3 = name1.count("u")
count4 = name1.count("e")
true1_count = count1 + count2 + count3 + count4
count5 = name1.count("l")
count6 = name1.count("o")
count7 = name1.count("v")
count8 = name1.count("e")
love1_count = count5 + count6 + count7 + count8

# Calculate the total for name1
name1_total = int(str(true1_count) + str(love1_count))

# Calculate the occurrence counts for 'true' and 'love' in name2

# true2_count = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
# love2_count = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

count1 = name2.count("t")
count2 = name2.count("r")
count3 = name2.count("u")
count4 = name2.count("e")
true2_count = count1 + count2 + count3 + count4
count5 = name2.count("l")
count6 = name2.count("o")
count7 = name2.count("v")
count8 = name2.count("e")
love2_count = count5 + count6 + count7 + count8

# Calculate the total for name2
name2_total = int(str(true2_count) + str(love2_count))

# Calculate the love score
love_score = name1_total + name2_total


# Output love score interpretation
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


# In[ ]:





# In[ ]:





# In[ ]:





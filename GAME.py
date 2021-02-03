#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import numpy as np
random_number = np.random.randint(1, 101) 
print (f"Сгенерировано число от {1} до {100}")
iteration_count=int()
def random_function(random_number):
    count = 0
    left = range_start 
    right = range_end  
    predict = 0
    while predict != random_number:    
        count += 1       
        predict = (left+right) // 2       
        if random_number == predict: break  
        elif random_number > predict: 
            left = predict +1
        elif random_number < predict: 
            right = predict -1
    return(count)
print (f"Алгоритм угадал число {random_number} за {random_function(random_number)} попыток")  
def mean_count(random_function):
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_list.append(random_function(random_number))
    score = int(np.mean(count_list))
    return(score)
print(f"Алгоритм угадывает число в среднем за {random_function(random_number)} попыток")


# In[ ]:





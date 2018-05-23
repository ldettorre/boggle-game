# List Comprehension Challenges
# Example:
# Question 
#                 range(10) 
#                 -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Answer
#                 [n * 2 for i in range(10)]
# 1. range(5) 
# -> ["*", "*", "*", "*", "*"]
# 2. ["Hi", "There", "Everyone"] 
# -> [2, 5, 8]
# 3. range(8) 
# -> [0, 1, 4, 9, 16, 25, 36, 49]
# 4. range(5) 
# -> [(0,1), (1,2), (2,3), (3,4), (4,5)]
# 5. 'woohoo' 
# -> ['w', 'o', 'o', 'h', 'o', 'o']
# 6. ['car', 'cat', 'maps', 'if', 'level'] 
# -> [('car', 3), ('cat', 3), ('maps', 4), ('if', 2), ('level', 5)]
# 7. [(False, False), (False, True), (True, False), (True, True)]
# ->[False, False, False, True]
# 8. [(False, False), (False, True), (True, False), (True, True)]
# ->[False, True, True, True]

# challenge 1
# print["*" for i in range(6)]

#challenge 2
# words =  ["Hi", "There", "Everyone"]
# print ([len(i) for i in words])

#challenge 3
# print([i*i for i in range(8)])

#challenge 4
# print([ (i,i+1) for i in range(5)])

#challenge 5
# print([ i for i in "woohoo"])

#challenge 6
# words = ['car', 'cat', 'maps', 'if', 'level']
# print([(i,len(i)) for i in words])

# Dictionary Comprehension Challenges
# Example:
# Question 
#                 range(5) 
#                 -> { 0: "", 1:"*", 2:"**", 3:"***", 4:"****" }
# Answer
#                 { i:"*" * i for i in range(5)}
# 1. ['Hi', 'There', 'Everyone'] 
# -> {'Hi':2, 'There':5, 'Everyone':8}
# 2. 'code'
# -> {'c': 99, 'e': 101, 'd': 100, 'o': 111}
# 3. ['car', 'cat', 'maps', 'if', 'level'] 
# -> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}


# lst =[]
# type(lst)

# i = 0
# def filter_long_words(n):
#     n = int(input("Enter number of elements : ")) 
  
# # iterating till the range 
#     for i in range(0, n): 
#         ele = int(input()) 
    
#         lst.append(ele) # adding the element 
      
# print(lst) 

listOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
 
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
 
print ("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))

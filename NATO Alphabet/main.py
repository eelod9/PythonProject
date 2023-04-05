'''
List comprehension
numbers = [1,2,3]
new_list = [i+1 for i in numbers]
print(new_list)

name = "Ella"
new_list2 = [i for i in name]

new_list3 = [k*2 for k in range(1,5) if k%2 ==0]
print(new_list3)
'''
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}



test = {
    "Angela": 78,
    "Ella": 90,
    "Clara": 80
}
passed_students = {s:v for (s,v) in test.items() if v>79}
print(passed_students)

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("./NATO Alphabet/nato_phonetic_alphabet.csv")


nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(nato_dict)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("enter word: ").upper()
result = [nato_dict[i] for i in user_input  ]
print(result)
# with open("ex_list.txt", 'r') as file_1, open("sol_list.txt", "a") as file_2:
#   for line in file_1:
#     if ("Solution:") in line:
#       file_2.write(line)
#     else:
#       print("not in line bro")

cur_line = 0 
starting_lines = []
ending_lines = []
final_lines = []
i = 1


with open("ex_list.txt", 'r') as file_1, open("sol_list.txt", "a") as file_2:
  for line in file_1:
    cur_line += 1
    if ("Solution") in line:
      starting_lines.append(str(cur_line))
      file_2.write(line)
    elif ("Question") in line:
      ending_lines.append(str(cur_line))
      file_2.write(line)


print(", ".join(starting_lines)) 
print(", ".join(ending_lines))

print(f"There are {len(starting_lines)} Questions") #well, there seems to be more solutions than answers... so this project is a faliure
print(f"There are {len(ending_lines)} Solutions") 


#original plan:
#Ending line[i] - Starting line[i] to get the number of lines we need to read.

#then, for lines in range (number of lines we need to read) from starting_line to ending_line:
#file_2.write(f"{i}:\n {lines}")

#this project has come to a close, failed. 

def main():

  print_line = False
  solution_number = 1

  with open("ex_list.txt", 'r') as file_1, open("sol_list.txt", "w") as file_2:
    for line in file_1:

      '''
      Once we have reached a solution, start printing
      '''
      if "Solution" in line:

        file_2.write(f"\nSolution: {solution_number}\n")
        #sys.stdout.write(f"Solution: {solution_number}")
        
        solution_number += 1 
        print_line = True;
        continue

      '''
      Print until end of solution has been reached
      '''
      if print_line:
        if "#----------------------------------------#" in line:
          print_line = False;
          continue
        
        file_2.write(line)
        
    return("It is successful")

def py2_3(): #converts python 2 to python 3
  
  original = "raw_input"
  new = "input"
  
  # Read in the file
  with open('sol_list.txt', 'r') as file_1 :
    filedata = file_1.read()

  # Replace raw_input with input
  filedata = filedata.replace(original, new)

  # Write the file out again
  with open('sol_list.txt', 'w') as file_1:
    file_1.write(filedata)
    
   
if __name__ == '__main__':
  print(main())
  py2_3()



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
    
if __name__ == '__main__':
  print(main())

from datetime import datetime

# datetime object containing current date and time
date = datetime.now()
# dd/mm/YY H:M:S
dt_string = date.strftime("%d/%m/%Y %H:%M:%S")

#get input/output file from user
INPUT_FILE = input("enter input file: ")
OUTPUT_FILE = input("enter output_file name: ")

def main():

  print_line = False
  number = 1
  
  #get inputs from user
  starting_word = input("enter starting word: ")
  ending_word = input("enter ending word: ")
  
  #log the date, starting_word, ending_word, input file and output file
  with open("log.txt", "a") as log: 
    log.write(f"\n\n Date: {date} \nStarting Word: {starting_word} \nEnding Word:{ending_word}\nInput File:{INPUT_FILE}\nOutput File:{OUTPUT_FILE}")
    log.close() #close the log
  
  
  with open(INPUT_FILE, 'r') as file_1, open(OUTPUT_FILE, "w") as file_2:
    for line in file_1:

      '''
      Once we have reached a solution, start printing
      '''
      if starting_word in line:

        file_2.write(f"\n{starting_word}: {number}\n")
        
        number += 1 
        print_line = True;
        continue

      '''
      Print until end of solution has been reached
      '''
      if print_line:
        if ending_word in line:
          print_line = False;
          continue
        
        file_2.write(line)
        file_1.close() #close both files
        file_2.close() 
        
    return("It is successful")


def word_convert():
  
  original = input("what word would you like to replace: ")
  new = ("What word do you want to replace it with: ")
  
  # Read in the file
  with open(INPUT_FILE, 'r') as file_1 :
    filedata = file_1.read()

  # Replace raw_input with input
  filedata = filedata.replace(original, new)

  # Write the file out again
  with open(INPUT_FILE, 'w') as file_1:
    file_1.write(filedata)
    
   
if __name__ == '__main__':
  print(main())
#   word_convert()



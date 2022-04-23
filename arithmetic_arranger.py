def arithmetic_arranger(problems,answers = False):
  
  dash = "-"
  space = " "
  
  #initialize the lines needed
  line1 = []
  line2 = []
  line3 = []
  line4 = []

  first = True
  
  #check if there are too many problems supplied
  if len(problems) > 5:
    return("Error: Too many problems.")

  #operator declaration
  operators = ("+", "-")

  #split the different arithmetic functions
  for value in problems:
    problemSplit = value.split(" ")
  
    #check if operator is permitted
    if problemSplit[1] not in operators:
      return("Error: Operator must be '+' or '-'.")
  
    #check if operands are digits
    if not (problemSplit[0].isdigit() and problemSplit[2].isdigit()):
      return("Error: Numbers must only contain digits.")
    
    #check if each operand has no more than 4 digits
    if len(problemSplit[0]) > 4 or len(problemSplit[2]) > 4:
      return("Error: Numbers cannot be more than four digits.")

    # find the longest of the two operands to get the max number of spaces in the lines + two additional spaces for operator and a free space between operators and operands
    spaces_needed = max(len(problemSplit[0]),len(problemSplit[2]))+2

    #check if it is the first problem
    if first == True:
    
      #fill in lines in line3 with appropriate amount of dashes
      #line3.append(dash*spaces_needed + space*4)
      line3 = dash*spaces_needed
    
      #fill in the lines 1 & 2 with operands, operators and the appropriate amount of spaces
      spaces_needed_line1 = spaces_needed - len(problemSplit[0])
      line1 = space*spaces_needed_line1 + problemSplit[0]

      spaces_needed_line2 = spaces_needed - 2 - len(problemSplit[2])
      line2 = problemSplit[1] + space + space*spaces_needed_line2 + problemSplit[2]

      #fill in the result line, if needed
      result = str(eval(value))
      spaces_needed_line4 = spaces_needed - len(result) 
      line4 = space*spaces_needed_line4 + str(result)

      first = False

    else:
      #fill in lines in line3 with appropriate amount of dashes
      #line3.append(dash*spaces_needed + space*4)
      line3 = space* 4 + dash*spaces_needed
    
      #fill in the lines 1 & 2 with operands, operators and the appropriate amount of spaces
      spaces_needed_line1 = spaces_needed - len(problemSplit[0])
      line1 = space*4 + space*spaces_needed_line1 + problemSplit[0]

      spaces_needed_line2 = spaces_needed - 2 - len(problemSplit[2])
      line2 = space*4 + problemSplit[1] + space + space*spaces_needed_line2 + problemSplit[2]

      #fill in the result line, if needed
      result = str(eval(value))
      spaces_needed_line4 = spaces_needed - len(result) 
      line4 = space*4 + space*spaces_needed_line4 + str(result)
  
  # return the arranged problems
  if answers == True:
    return line1 + "\n" + line2 + "\n" + line3 + "\n"+ line4
  else:
    return line1 + "\n" + line2 + "\n"+ line3
    

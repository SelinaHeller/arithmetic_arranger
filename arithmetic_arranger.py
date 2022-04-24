def arithmetic_arranger(problems,answers = False):
  
  dash = "-"
  space = " "
  
  #initialize the lines needed
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  
  #check if there are too many problems supplied
  if len(problems) > 5:
    return("Error: Too many problems.")

  #operator declaration
  operators = ("+", "-")

  #split the different arithmetic functions
  for index,problem in enumerate(problems):
    problemSplit = problem.split(" ")

    operand1 = problemSplit[0]
    operand2 = problemSplit[2]
    operator = problemSplit[1]
  
    #check if operator is permitted
    if operator not in operators:
      return("Error: Operator must be '+' or '-'.")
  
    #check if operands are digits
    if not (operand1.isdigit() and operand2.isdigit()):
      return("Error: Numbers must only contain digits.")
    
    #check if each operand has no more than 4 digits
    if len(operand1) > 4 or len(operand2) > 4:
      return("Error: Numbers cannot be more than four digits.")

    # find the longest of the two operands to get the max number of spaces in the lines + two additional spaces for operator and a free space between operators and operands
    spaces_needed = max(len(operand1),len(operand2))+2

    #fill in lines in line3 with appropriate amount of dashes
    #line3.append(dash*spaces_needed + space*4)
    line3 = dash*spaces_needed
    
    #fill in the lines 1 & 2 with operands, operators and the appropriate amount of spaces
    spaces_needed_line1 = spaces_needed - len(operand1)
    line1 = space*spaces_needed_line1 + operand1

    spaces_needed_line2 = spaces_needed - 2 - len(operand2)
    line2 = operator + space + space*spaces_needed_line2 + operand2

    #fill in the result line, if needed
    result = str(eval(problem))
    spaces_needed_line4 = spaces_needed - len(result) 
    line4 = space*spaces_needed_line4 + str(result)

    if (index < len(problems) - 1):
      #fill in lines in line3 with appropriate amount of dashes
      #line3.append(dash*spaces_needed + space*4)
      line3 = space* 4 + dash*spaces_needed
    
      #fill in the lines 1 & 2 with operands, operators and the appropriate amount of spaces
      spaces_needed_line1 = spaces_needed - len(operand1)
      line1 = space*4 + space*spaces_needed_line1 + operand1

      spaces_needed_line2 = spaces_needed - 2 - len(operand2)
      line2 = space*4 + operator + space + space*spaces_needed_line2 + operand2

      #fill in the result line, if needed
      result = str(eval(problem))
      spaces_needed_line4 = spaces_needed - len(result) 
      line4 = space*4 + space*spaces_needed_line4 + str(result)
      
  # return the arranged problems
  if answers:
    print(line1 + "\n" + line2 + "\n" + line3 + "\n"+ line4)
    return line1 + "\n" + line2 + "\n" + line3 + "\n"+ line4
  else:
    print(line1 + "\n" + line2 + "\n" + line3)
    return line1 + "\n" + line2 + "\n"+ line3
    
    

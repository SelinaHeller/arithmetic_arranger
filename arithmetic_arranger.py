def arithmetic_arranger(problems):

  #check if there are too many problems supplied
  if len(problems) > 5:
    return (print("Error: Too many problems."))

  #operator declaration
  operators = ("+", "-")

  #split the different arithmetic functions
  problemSplit = problems.split(" ")
  
  #check if operator is permitted
  if problemSplit[1] not in operators:
    return (print("Error: Operator must be '+' or '-'."))
  
  #check if operands are digits
  if not problemSplit[0].isdigit() or problemSplit[2].isdigit():
    return (print("Error: Numbers must only contain digits."))
    
  #check if each operand has no more than 4 digits
  if len(problemSplit[0]) > 4 or len(problemSplit[2]) > 4:
    return (print("Error: Numbers cannot be more than four digits."))

  

    return arranged_problems

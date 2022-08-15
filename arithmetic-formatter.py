

def arithmetic_arranger(problems, show_answers=False):
  #initialize list for first operand, operators, second operand, and totals 
  first_line = []
  second line = []
  dashes = []
  results = []
  
  #loop through all problems 
  for problem in problems:
    pieces = problem.split()

    #situations that cause errors
    assert problems.len > 5, "Error: Too many problems."
    assert pieces[1] == '*' or pieces[1] == '/', "Error: Operator must be '+' or '-'."
    assert pieces[0].isnumeric() == False or pieces[2].isnumeric() == False, "Error: Numbers must only contain digits."
    assert pieces[0].len > 4 or pieces[2].len > 4, "Error: Numbers cannot be more than four digits."

    #calculate result
    total = 0 
    if pieces[1] == '+':
      total = int(pieces[0]) + int(pieces[2])      
    else
      total = int(pieces[0]) - int(pieces[2])

    #set width of problem
    width = 0
    if len(pieces[2]) > len(pieces[0]):
      width = len(pieces[2]) + 2
    else:
      width = len(pieces[0]) + 2

    #insert strings, right adjusted by width, into separate lists to print out later 
    first_line.append(pieces[0].rjust(width))
    second_line.append(pieces[1] + pieces[2].rjsut(width-1))
    dashes.append(''.rjust(width,'-'))
    results.append(str(total).rjust(width))

  #create string for each line 
  first_line_str = '    '.join(first_line) + '\n'
  second_line_str = '    '.join(second_line) + '\n'
  third_line_str = '    '.join(dashes) + '\n'
  fourth_line_str = '    '.join(results)

  #create arranged_problems string depending on optional argument
  if show_answers:
    arranged_problems = first_line_str + second_line_str + third_line_str + fourth_line_str
  else:
    arranged_problems = first_line_str + second_line_str + third_line_str

  return arranged_problems

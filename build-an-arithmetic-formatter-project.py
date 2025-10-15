** start of main.py **

# The entire thing is just a function definition, so just
# call the function with a list of problems.

# I recommend creating a problems variable and playing with the function before
# trying to read the code

# the problems should have a format as follows:
# problems = ['3 - 2', '9999 - 400', '1 + 1', '32 + 64'],
# and if you print the function call with your problems
# it'll display them in a neat format or display a simple error message
# if you break the rules imposed by the project.

# use True as the second attribute to display the answers, might as well

def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return 'Error: Too many problems.'

    output_length = len(problems)

    # if I find the first space in each string, I can create two lists containing 
    # the numbers by themselves which I thought would be easier to work with 
    
    first_operands = []
    for problem in problems:
        if not problem[:problem.find(' '):].isdigit():
            return 'Error: Numbers must only contain digits.'
        first_operands.append(int(problem[:problem.find(' '):]))
    second_operands = []
    
    for problem in problems:
        if not problem[problem.find(' ') + 3::].isdigit():
            return 'Error: Numbers must only contain digits.'
        second_operands.append(int(problem[problem.find(' ') + 3::]))
    
    for digit in first_operands:
            
        if len(str(digit)) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    for digit in second_operands:
        
        if len(str(digit)) > 4:
            return 'Error: Numbers cannot be more than four digits.' 

    # decided to create a list that holds just the operations
    # for formatting purposes

    
    problem_type = []
    for problem in problems:
        problem_type.append(problem[problem.find(' ') + 1])

    
    for operation in problem_type:
        if operation != '+' and operation != '-':
            return "Error: Operator must be '+' or '-'."

    
    # although quite short, this function helps me right-align numbers
    # without having to give a shit about how long the numbers are
    
    
    def right_align(current, other):
        space = ' ' * (len(str(max(current, other))) - len(str(current)))
        return space 

    
    # this is where the output construction actually happens and it's 
    # definitely the most embarassing code segment.

    # the strategy I landed on was to create 'cells' that could be repeated
    
    
    indent = '    '   
    line1_cells = ['  ' + right_align(top,bottom) + str(first_operands[first_operands.index(top)]) + indent for top, bottom in zip(first_operands, second_operands)]
    
    line2_cells = [problem_type[second_operands.index(bottom)] + ' ' + right_align(bottom, top) + str(second_operands[second_operands.index(bottom)]) + indent for top, bottom in zip(first_operands, second_operands)]
    
    line3_cells = [('-' * (2 + len(str(max(top, bottom))))) + indent for top, bottom in zip(first_operands, second_operands)]
    
    line4_cells = [(' ' * (2 + len(str(max(top, bottom))) - len(str(top + bottom if problem_type[second_operands.index(bottom)] == '+' else top - bottom )))) + str((top + bottom) if problem_type[second_operands.index(bottom)] == '+' else (top - bottom)) + indent for top, bottom in zip(first_operands, second_operands)]
 
    # Now I'm just taking my lists and joining the elements into strings
    
    line1 = ''.join(line1_cells)
    line2 = ''.join(line2_cells)
    line3 = ''.join(line3_cells)
    line4 = ''.join(line4_cells)
    
    # The magic number '-4' appears because I'm slicing off the idents at the end of the last cell
        
    formatted_problems = line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]
    if show_answers:
        formatted_problems += '\n' + line4[:-4]
    
    return formatted_problems

# completed at 2AM Sunday, October 5th, 2025

** end of main.py **


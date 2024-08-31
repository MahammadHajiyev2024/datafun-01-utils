''' Iteration 2 - improve byline

Module: Mo is doing Analytics

Process:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
2. I'll declare a global variable for my byline string and just set it to some simple text.
3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.
4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''
#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Mo is doing Analytics'

#####################################
#Define the get_byline() function
#####################################

def get_byline() -> str:
    '''Return the byline for my analytics project'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()

'''
Setting path at Windows :
To add the Python directory to the path for a particular session in Windows - 
At the command prompt - type path %path%;C:\Python and press Enter.

Note : C:\Python is the path of the Python directory
'''
######## Environment Variables in Python  #######
'''
PYTHONPATH :
     it has a role similar to PATH.
     This variable tells the Python interpreter where to locate the module file imported into program.
     It should include the Python source library directory and the directories containing Python source code.
     PYTHONPATH is sometimes preset by the Python installer.
PYTHONSTARTUP :
     It contains the path of an initialization file containing Python source code.
     It is excuted every time you start the interpreter. 
     It is named as .pythonrc.py in Unix and it contains commands that load utilities or modify PYTHONPATH
PYTHONCASEOK
     It is used in Windows to instruct Python to find the first case-insensitive match in an import statement.
     Set this variable to any value to activate it.
PYTHONHOME
     It is an alternative module search path. It is usually embedded in the PYTHONSTARTUP or PYTHONPATH directories to make switching module libraries easy.


'''
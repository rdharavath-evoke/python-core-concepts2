##### Modes of files #####
# r : Opens a files for reading. (default)
# w : Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x : Opens a file for exclusive creation. If the file already exists, the operation fails.
# a : Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t : Opens in text mode. (default)
# b : Opens in binary mode.
# + : Opens a file for updating (reading and writing) 


'''
Python provides inbuilt functions for creating, writing and reading files.
There are two types of files that can be handled in python
1.text files
2.birary files(written in binary language, 0s and 1s)


Text files : In this type of file, Each line of text is terminated with a special charecter called EOL(End Of Line)
             Which is the new line charecter ('\n') in python by default.
Binary files : In this type of file, there is no terminator for a line and the data is stored after converting
               it into machine understandable binary language. 
'''
       
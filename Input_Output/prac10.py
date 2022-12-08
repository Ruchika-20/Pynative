############################################################################
# QUESTION 10 : Read line number 4 from the following file                 #
############################################################################

# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])



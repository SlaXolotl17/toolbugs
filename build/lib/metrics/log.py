class Log:
    def __init__(self, file):
        self.file = open(file, "a")
        self.file.write("New log created.\n")
    
    def logVariable(self, variable, namespace):
        varname = ""
        for name, value in namespace.items():
            if value is variable:
                varname = name
        self.file.write(f"Variable {varname} is set to {variable}.\n")

    def logFunction(self, function, *fnargs):
        funcname = function.__name__
        try:
            result = function(*fnargs)
            self.file.write(f"Output of {funcname} with arguments {fnargs} is {result}.\n")
        except Exception as e:
            self.file.write(f"{type(e).__name__} occurred while calculating output of {funcname} with arguments {fnargs}: {e}.\n")

    def endLog(self):
        self.file.write("End of log.")
        self.file.close()

def newLog(filename):
    '''
    creates a new log tied to a file
    Parameters:
        filename (str): the name of the file to be used as a log. should not include a file extension.
    '''
    log = Log(filename + ".txt")
    return log
import sys 

class CsvReader():
    def __init__(self, filename=None, sep='', header=False, skip_top=0, skip_bottom=0):
    # ... Your code here ...
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        # ... Your code here ...
        try:
            self.files = open(self.filename, "r")
        except FileNotFoundError as error_msg:
            print(error_msg, file=sys.stderr)
            sys.exit()
        else:
            lines = self.files.readlines()
            if self.header:
                lines = lines[self.skip_top:]
            if self.skip_bottom:
                lines = lines[:-self.skip_top]
            for line in lines:
                field = line.strip().split(self.sep)
                self.data.append(field)
        return self
        

    def __exit__(self, type, value, traceback):
     # ... Your code here ...
        self.files.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """

        return self.data if  self.data[0]  else None
    
if __name__ == "__main__":
    print("hello")
    with CsvReader (filename="file.csv", sep=",") as file:
        data  = file.getdata()
        print(data)

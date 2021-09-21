class LogParser():
    def __init__(self, file) -> None:
        self.file_name = file
        self.file_handle = None
        self.time_min = 0
        self.time = ''
        self.content = ''
        self.open_file()
        return None

    def open_file(self):
        with open(self.file_name, 'rt') as f:
            self.content = f.read()

    def time_cal(self): 
        self.time = str(int((self.time_min/60)))+'hr '+str(self.time_min%60) + 'mins'

    def reset(self) -> None:
        self.time_min = 0

        return None

    #TODO: parse funtion
    def parse(log_file):
        print('Parsing..')
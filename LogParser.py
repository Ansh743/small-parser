#author - Anshul Maske (2830914)
class LogParser():
    def __init__(self, file) -> None:
        self.file_name = file
        self.time_min = 0
        self.time_hr = 0
        self.time = ''
        self.content = ''
        self.open_file()
        self.start = ''
        self.stop = ''
        return None

    def calcuate(self):
        smin = int(self.start[-2:])
        emin = int(self.stop[-2:])
        shr = int((self.start[:2].strip()))
        ehr = int((self.stop[:2].strip()))
        mins = 0
        hrs = 0
        if smin > emin:
            mins = 60 - (smin-emin)
            hrs -= 1
        else:
            mins = emin - smin

        if shr > ehr:
            hrs = hrs + (12 - (shr - ehr))
        else:
            hrs = hrs + ehr - shr
        
        #print(self.start, self.stop, hrs,'hr ', mins, 'mins')
        self.time_hr += hrs
        self.time_min += mins 

    def open_file(self):
        with open(self.file_name, 'r') as f:
            self.content = f.read()

    def time_cal(self):
        self.time_hr += (self.time_min//60)
        self.time_min = (self.time_min%60)
        self.time = str(self.time_hr)+' hours '+str(self.time_min)+' minutes'

    def reset(self) -> None:
        self.time_min = 0
        self.time = 0

        return None

    def parse(self):
        con = self.content

        clear_back_index = con.index('Time Log:')
        con = con[clear_back_index::]
        con = con.lower()
        individual_lines = con.splitlines()
        
        for line in individual_lines:
            if 'am' in line or 'pm' in line:
                flag = 0
                for i in range(len(line)):
                    if flag > 2:
                        self.start = ''
                        self.stop = ''
                        break
                    if flag == 0 and (line[i:i+2].__eq__('am') or line[i:i+2].__eq__('pm')):
                        self.start = line[i-5:i]
                        flag += 1
                    elif flag == 1 and (line[i:i+2].__eq__('am') or line[i:i+2].__eq__('pm')):
                        self.stop = line[i-5:i]
                        flag += 1
                    elif flag == 2:
                        self.calcuate()
                        flag = 0
                        break
            else:
                pass
        self.time_cal()
        return self.time
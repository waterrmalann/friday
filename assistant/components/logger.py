import enum
import datetime

class LogChannels(enum.Enum):
    Output = 1
    Input = 2
    Error = 3
    Debug = 4

class SessionLogger:
    """
    Plugs into the assistant and logs all input, output, error streams.
    Do not use. Use python's in-built module 'logger' instead.
    """

    def __init__(self, path):
        self.path = path
        self.log_threshold = 128
        self.save_logs = True

        self.output_path = ''
        self.input_path = ''
        self.error_path = ''
        self.debug_path = ''

        self.err_logs = []
        self.out_logs = []
        self.in_logs = []
        self.debug_logs = []
    
    def create_log_files(self):
        f = open(self.output_path, 'w').close()
        f = open(self.input_path, 'w').close()
        f = open(self.error_path, 'w').close()
        f = open(self.debug_path, 'w').close()

    def outlog(self, log:str):
        now = datetime.datetime.now()
        l = f"[{now.strftime('%H:%M:%S')}] {log}"
        self.out_logs.append(l)
    
    def inlog(self, log:str):
        now = datetime.datetime.now()
        l = f"[{now.strftime('%H:%M:%S')}] {log}"
        self.in_logs.append(l)
    
    def debuglog(self, log:str):
        now = datetime.datetime.now()
        l = f"[{now.strftime('%H:%M:%S')}] {log}"
        self.debug_logs.append(l)

    def errlog(self, log:str):
        now = datetime.datetime.now()
        l = f"[{now.strftime('%H:%M:%S')}] {log}"
        self.err_logs.append(l)
    
    

        
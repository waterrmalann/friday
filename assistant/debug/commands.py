# todo: commands could raise BadArguments() / MissingArguments()

def cmd_ping(assistant, *args):
    print("Pong!")

def cmd_help(assistant, *args):
    print("/ping: Get latency.")
import sys
# Prevent the writing of .pyc files.
# It helps but we don't really need those during development. Just helps the file structure stay cleaner.
sys.dont_write_bytecode = True

import assistant
import logging
import tomli

with open('config.toml', 'rb') as f:
    config = tomli.load(f)

friday = assistant.Assistant(
    name = config['assistant']['name'],
    config = config, 
    log_handler = logging.FileHandler("logs/log.log", "w", "utf-8")
)

print(r" ____  ___   _   ___    __    _    ")
print(r"| |_  | |_) | | | | \  / /\  \ \_/ ")
print(r"|_|   |_| \ |_| |_|_/ /_/--\  |_|  ")
print()

# Simple input listener.
while True:
    # Get typed input from the user.
    inp = input("You: ")

    # Send the user input to the assistant and obtain a result.
    result = friday.process(inp)

    # Check if the result is multi-line or single line and print accordingly.
    if isinstance(result, list):
        print(friday.name + ': ' +  '\n'.join(result))
    else:
        print(friday.name + ': ' + result)

    print()
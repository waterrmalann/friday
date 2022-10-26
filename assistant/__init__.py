import os
import logging
import datetime
import time

from assistant.utils.ticker import Ticker
from assistant.components.threads import EventLoop, Scheduler
from assistant.components.interpreter import IntentInterpreter
from assistant.handlers.command_handler import CommandHandler
from assistant.handlers.request_handler import RequestHandler

from assistant.debug.commands import cmd_help, cmd_ping

class Assistant:
    def __init__(self, name, config, log_handler=None):

        # Name of the assistant (used internally).
        self.name = name

        self.start_time = time.time()

        # Base configuration. Usually the config.toml file.
        self.config = config

        # Get the current working directory of the driver program.
        # Helps figure out where everything else is.
        self.cwd = os.getcwd()

        # Set up logger
        formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', '%H:%M:%S', style='{')
        handler = log_handler or logging.StreamHandler()
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

        self.memory = []

        self.interpreter = IntentInterpreter(self)
        # Note: The order in which the handlers are attached is important as some handlers may practically accept anything.

        # Command Handlers
        self.interpreter.attach_handler(CommandHandler(cmd_help, ('info', 'help')))
        self.interpreter.attach_handler(CommandHandler(cmd_ping, ('ping', 'latency')))
        
        # Request Handler
        self.interpreter.attach_handler(RequestHandler()) # -> perhaps the engine can be put inside this


        self.logger.info("Assistant Initialized")

        self.mainloop = EventLoop(self.config['developer']['main_loop_delay'])
        self.mainloop.add_function(self.loop)

        self.scheduler = Scheduler(self.config['developer']['sched_loop_delay'])

        self.ticks = 0
        self.launch_time = datetime.utcnow()

        self.mainloop.start()
        self.scheduler.start()

    def process(self, msg):
        """Pipe user input to the intent interpreter."""
        
        self.on_update()

        response = self.interpreter.process(msg)
        
        self.logger.info(f"User: {msg}")
        self.logger.info(f"{self.name}: {response.content}")

        return response.content
    
    def get_uptime(self):
        """Returns the number of seconds has it been since the assistant was started."""

        return time.time() - self.start_time

    def loop(self):
        self.ticks += 1
        os.system(f"title Friday: Desktop Virtual Assistant ^| Tick {self.ticks}")
    
    def on_update(self):
        pass


# assistant.interpreter.handlers['CommandHandler'].register_command = 
import os
from assistant.datatypes.message import Message
from assistant.engines import SRE, SBRE
import logging

class Assistant:
    def __init__(self, name, config, log_handler=None):

        # Name of the assistant (used internally).
        self.name = name

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

        # Skill-Based Response Engine (SBRE) is the modular and extendable response engine.
        self.engine = SBRE.SkillBasedResponseEngine(self)
        # self.engine = SRE.SimpletonResponseEngine(self)

        self.logger.info("Assistant Initialized")

    def process(self, msg):
        """Processes input obtained from the user into something the assistant can understand and returns a result."""
        
        # Process the user input.
        processed = Message(msg)

        # Pass it to the active engine.
        response = self.engine(processed)

        self.logger.info(f"User: {msg}")
        self.logger.info(f"{self.name}: {response.content}")

        return response.content

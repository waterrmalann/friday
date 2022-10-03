from assistant.handlers import Handler
from assistant.datatypes.message import Message
from assistant.engines import SRE, SBRE

class RequestHandler(Handler):

    def __init__(self):
        super().__init__("Request Handler")

        self.engine = None
    
    # todo: def load_engine, unload_engine, reload_engine, set_engine
    def setup(self, interpreter):
        super().setup(interpreter)

        # todo: No default engine or attach_engine() or smth like that in setup()
        # Skill-Based Response Engine (SBRE) is the modular and extendable response engine.
        self.engine = SBRE.SkillBasedResponseEngine(self.assistant)
    
    def handle(self, message):
        msg = Message(message)
        return self.engine(msg)
    
    def check(self, message):
        return True
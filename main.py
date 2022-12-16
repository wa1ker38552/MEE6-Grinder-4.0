from handler import Handler
from client import Client
import os


TOKEN1 = Client(os.environ['TOKEN1'])
TOKEN2 = Client(os.environ['TOKEN2'])

TOKEN2._config.hours.time = (6, 15)

handle = Handler([TOKEN1, TOKEN2],
                 counting=[True, True], 
                 economy=[True, True],
                 offset=1800)

handle.start()

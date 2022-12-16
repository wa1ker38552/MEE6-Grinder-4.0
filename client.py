class Economy:
  def __init__(self):
    # default economy configurations
    self.interval = 3600
    self.randomization = (0, 5)
    self.channel = 867990271042916412
    self.messages = ['!work claim', '!work']
    self.messages_randomization = (1, 30)

class Counting:
  def __init__(self):
    # default counting configurations
    self.interval = 60
    self.randomization = 0.2
    self.channel = 1015923752422346782

class Hours:
  def __init__(self):
    self.time = (8, 14)
    self.hour_variation = (0, 2)
    self.minute_variation = (0, 30)

class Configs:
  def __init__(self):
    # default configurations for bot
    self.economy = Economy()
    self.counting = Counting()
    self.hours = Hours()

class Client:
  def __init__(self, token):
    self._token = token
    self._config = Configs()

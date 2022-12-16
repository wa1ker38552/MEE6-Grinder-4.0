from threading import Thread
from alive import keepAlive
import autocord
import random
import time


class Handler:
  def __init__(self, clients: list, counting: list, economy: list, offset=0):
    self._client_settings = [cli._config for cli in clients]
    self._clients = [autocord.client(cli._token) for cli in clients]
    self._economy = economy
    self._counting = counting
    self._offset = offset
    self._offset_variance = (0, offset)
  
  def start(self):
    for i, client in enumerate(self._clients):
      if self._economy[i] is True:
        variance = random.randint(self._offset_variance[0], self._offset_variance[1])*i
        Thread(target=lambda: self.Economy(i, variance)).start()
      if self._counting[i] is True:
        Thread(target=lambda: self.Counting(i)).start()
    keepAlive()

  def Economy(self, client_index, offset):
    settings = self._client_settings[client_index]
    hours = list(range(settings.hours.time[0], settings.hours.time[1]))
    time.sleep(offset)

    def run_loop():
      for message in settings.economy.messages:
        self._clients[client_index].SEND_MESSAGE(message, settings.economy.channel)
        time.sleep(random.randint(settings.economy.messages_randomization[0], settings.economy.messages_randomization[1]))
      time.sleep(settings.economy.interval)
      time.sleep(random.randint(settings.economy.randomization[0], settings.economy.randomization[1])*60)
    
    while True:
      current_time = int(time.strftime("%H,%M,%S").split(',')[0])
      if current_time in hours:
        if current_time == hours[len(hours)-1] or current_time == hours[0]:
          time.sleep(random.randint(settings.hours.hour_variation[0], settings.hours.hour_variation[1])*3600)
          time.sleep(random.randint(settings.hours.minute_variation[0], settings.hours.minute_variation[1])*60)
          run_loop()
        else:
          time.sleep(60)
      else:
        run_loop()

  def Counting(self, client_index):
    settings = self._client_settings[client_index]
    hours = list(range(settings.hours.time[0], settings.hours.time[1]))
    util = autocord.utils(self._clients[client_index])
    
    def count():
      if random.randint(1, 100) <= settings.counting.randomization*100:
        history = util.FETCH_MESSAGE_HISTORY(settings.counting.channel, 1)
        if history[0].author.id != self._clients[client_index].id:
          try:
            current_count = int(history[0].content)
            self._clients[client_index].SEND_MESSAGE(current_count+1, settings.counting.channel)
          except ValueError: pass
      time.sleep(settings.counting.interval)

    while True:
      current_time = int(time.strftime("%H,%M,%S").split(',')[0])
      if current_time in hours:
        if current_time == hours[len(hours)-1] or current_time == hours[0]:
          time.sleep(random.randint(settings.hours.hour_variation[0], settings.hours.hour_variation[1])*3600)
          time.sleep(random.randint(settings.hours.minute_variation[0], settings.hours.minute_variation[1])*60)
          count()
        else:
          time.sleep(60)
      else:
        count()
      

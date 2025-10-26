from abc import ABC, abstractmethod

class IReader(ABC):
    @abstractmethod
    def read(self):
        raise NotImplementedError

class ISender(ABC):
    @abstractmethod
    def send(self):
        raise NotImplementedError

class DBReader(IReader):
    def read(self):
        print("Reading from DB")

class FileReader(IReader):
    def read(self):
        print("Reading from File")

class HTMLReader(IReader):
    def read(self):
        print("Reading from HTML")
      
  
class TelegramSender(ISender):
    def __init__(self, reader: IReader):
        self.reader = reader

    def send(self):
        self.reader.read()
        print("Sent to Telegram")


class EmailSender(ISender):
    def __init__(self, reader: IReader):
        self.reader = reader

    def send(self):
        self.reader.read()
        print("Sent to Email")
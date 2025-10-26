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
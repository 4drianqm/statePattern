from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def render(self):
        raise NotImplementedError

    @abstractmethod
    def publish(self):
        raise NotImplementedError

    @abstractmethod
    def approve(self):
        raise NotImplementedError

    @abstractmethod
    def unpublished(self):
        raise NotImplementedError

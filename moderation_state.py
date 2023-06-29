from state import State
from document import Document


class ModerationState(State):

    def __init__(self, document: Document):
        self.document = document

    def render(self):
        pass

    def publish(self):
        pass

    def approve(self):
        pass

    def unpublished(self):
        pass

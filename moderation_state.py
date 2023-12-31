from state import State
from document import Document


class ModerationState(State):

    def __init__(self):
        self.document: Document | None = None

    def set_document(self, document):
        self.document = document

    def render(self):
        print('---- EN MODERACION -----')
        print(self.document.name)
        print(self.document.content)
        print(f'Wrote by: {self.document.author.name}')

    def publish(self):
        pass

    def approve(self):
        pass

    def unpublished(self):
        pass

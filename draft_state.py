from state import State
from document import Document


class DraftState(State):

    def __init__(self, document: Document):
        self.document = document

    def render(self):
        print('---- EN REVISION -----')
        print(self.document.name)
        print(self.document.content)
        print(f'Wrote by: {self.document.author.name}')

    def publish(self):
        if self.document.author.role == 'admin':
            pass

    def approve(self):
        pass

    def unpublished(self):
        pass

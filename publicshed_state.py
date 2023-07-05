from state import State
from document import Document


class PublishedState(State):

    def __init__(self):
        self.document: Document | None = None

    def set_document(self, document: Document):
        self.document = document

    def render(self):
        print('---- PUBLISHED -----')
        print(self.document.name)
        print(self.document.content)
        print(f'Wrote by: {self.document.author.name}')

    def publish(self):
        published_state = PublishedState()
        self.document.change_state(published_state)
        published_state.set_document(self.document)

    def approve(self):
        pass

    def unpublished(self):
        pass

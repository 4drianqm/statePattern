from publicshed_state import PublishedState
from state import State
from document import Document
from moderation_state import ModerationState


class DraftState(State):

    def __init__(self):
        self.document: Document | None = None

    def set_document(self, document: Document):
        self.document = document

    def render(self):
        print('---- EN REVISION -----')
        print(self.document.name)
        print(self.document.content)
        print(f'Wrote by: {self.document.author.name}')

    def publish(self):
        if self.document.author.role == 'admin':
            published_state = PublishedState()
            self.document.change_state(published_state)
            published_state.set_document(self.document)
        else:
            moderation_state = ModerationState()
            self.document.change_state(moderation_state)
            moderation_state.set_document(self.document)

    def approve(self):
        pass

    def unpublished(self):
        pass

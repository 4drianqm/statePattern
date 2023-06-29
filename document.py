from user import User
from state import State
from draft_state import DraftState


class Document:
    def __init__(self,  name: str, content: str, author: User):
        self.name = name
        self.content = content
        self.author = author
        self.state: State = DraftState(self)

    def render(self):
        self.state.render()

    def publish(self):
        self.state.publish()

    def approve(self):
        self.state.approve()

    def unpublished(self):
        self.state.unpublished()

    def change_state(self, state: State):
        self.state = state

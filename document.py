from user import User
from state import State


class Document:
    def __init__(self,  name: str, content: str, author: User, state: State):
        self.name = name
        self.content = content
        self.author = author
        # modify initial state
        self.state: State = state
        self.state.set_document(self)

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

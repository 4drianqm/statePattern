from document import Document
from draft_state import DraftState
from user import User


author = User('Adrian', 'admin')
initial_stat = DraftState()
document = Document(
    'Hello world',
    'Content',
    author,
    initial_stat)

document.render()
document.publish()
document.render()

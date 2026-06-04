from ._anvil_designer import SubjectSelectTemplate
from anvil import *


class SubjectSelect(SubjectSelectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

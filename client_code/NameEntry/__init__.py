from ._anvil_designer import NameEntryTemplate
from anvil import *


class NameEntry(NameEntryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

from ._anvil_designer import LevelSelectTemplate
from anvil import *


class LevelSelect(LevelSelectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

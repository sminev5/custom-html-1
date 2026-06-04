from ._anvil_designer import TimeoutScreenTemplate
from anvil import *


class TimeoutScreen(TimeoutScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

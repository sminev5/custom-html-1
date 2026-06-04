from ._anvil_designer import WelcomeScreenTemplate
from anvil import *

class WelcomeScreen(WelcomeScreenTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_start_click(self, **event_args):
    open_form('NameEntry')
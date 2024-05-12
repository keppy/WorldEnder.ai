from prompt_toolkit import prompt, print_formatted_text, PromptSession, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig

DEFAULT_CONFIG = {
    'name': 'Player 1',
    'city': 'Seattle',
    'movement': 10,
    'skill': 'Survivalist',
    'item': 'Tools',
    'ailment': None,
    'hp': 100,
    'sanity': 100
}

def bottom_toolbar(player):
    return [('class:bottom-toolbar', f'Name: {player.name}, City: {player.city}')]

style = Style.from_dict({
    'bottom-toolbar': '#ffffff bg:#333333',
})

class Player(object):
    def __init__(self):
        self._values = DEFAULT_CONFIG
        self.session = PromptSession()

    @property
    def city(self):
        """The city property. A simple string, flexible on what's in it."""
        return self._values['city']

    @city.setter
    def city(self, value):
        """Set the underlying _values dictionary value for 'city'"""
        self._values['city'] = value

    @property
    def name(self):
        """The name property. A simple string."""
        return self._values['name']

    @name.setter
    def name(self, value):
        """Set the underlying _values dictionary value for 'name'"""
        self._values['name'] = value

    def prompt(self, htmlString):
        return self.session.prompt(HTML(htmlString), cursor=CursorShape.BLOCK, bottom_toolbar=bottom_toolbar(self))

    def getCity(self):
        self.city = self.prompt('<skyblue>What city will you begin your adventure in? </skyblue>')
        print_formatted_text(HTML(f'<springgreen>You are living in {self.city}</springgreen>'))

    def getName(self):
        self.name = self.prompt('<skyblue>What is your name? </skyblue>')
        print_formatted_text(HTML(f'<springgreen>Nice to meet you, {self.name}. Welcome to the WorldEnder.ai augmented reality simulation.</springgreen>'))

p = Player()
p.getName()
p.getCity()

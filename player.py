from prompt_toolkit import prompt, print_formatted_text, PromptSession, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig

DEFAULT_CONFIG = {
    'name': '',
    'city': '',
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

    @property
    def hp(self):
        """The hp property. An integer."""
        return self._values['hp']

    @hp.setter
    def hp(self, value):
        """Set the underlying _values dictionary value for 'hp'"""
        self._values['hp'] = value

    @property
    def sanity(self):
        """The sanity property. An integer."""
        return self._values['sanity']

    @sanity.setter
    def sanity(self, value):
        """Set the underlying _values dictionary value for 'sanity'"""
        self._values['sanity'] = value

    @property
    def item(self):
        """The item property. A string."""
        return self._values['item']

    @item.setter
    def item(self, value):
        """Set the underlying _values dictionary value for 'item'"""
        self._values['item'] = value

    @property
    def skill(self):
        """The skill property. A string."""
        return self._values['skill']

    @skill.setter
    def skill(self, value):
        """Set the underlying _values dictionary value for 'skill'"""
        self._values['skill'] = value

    @property
    def ailment(self):
        """The ailment property. A string."""
        return self._values['ailment']

    @ailment.setter
    def ailment(self, value):
        """Set the underlying _values dictionary value for 'ailment'"""
        self._values['ailment'] = value

    @property
    def movement(self):
        """The movement property. A string."""
        return self._values['movement']

    @movement.setter
    def movement(self, value):
        """Set the underlying _values dictionary value for 'movement'"""
        self._values['movement'] = value

    def prompt(self, htmlString):
        return self.session.prompt(HTML(htmlString), cursor=CursorShape.BLOCK, bottom_toolbar=bottom_toolbar(self))

    def get_city(self):
        self.city = self.prompt('<skyblue>What city will you begin your adventure in? </skyblue>')
        print_formatted_text(HTML(f'<springgreen>You are living in {self.city}</springgreen>'))

    def get_name(self):
        self.name = self.prompt('<skyblue>What is your name? </skyblue>')
        print_formatted_text(HTML(f'<springgreen>Nice to meet you, {self.name}. Welcome to the WorldEnder.ai augmented reality simulation.</springgreen>'))

    def statusbar_text(self):
        return f'''
            name: {self.name}          city: {self.city}
            movement: {self.movement}  skill: {self.skill}
            item: {self.item}          ailment: {self.ailment}
            hp: {self.hp}              sanity: {self.sanity}
        '''

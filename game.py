from prompt_toolkit import prompt, print_formatted_text, PromptSession, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig

def bottom_toolbar():
    return [('class:bottom-toolbar', ' This is a toolbar. ')]

style = Style.from_dict({
    'bottom-toolbar': '#ffffff bg:#333333',
})

class Player:
    def __init__(self):
        self.session = PromptSession()
        self.getName()
        self.getCity()

    def prompt(self, htmlString):
        return self.session.prompt(HTML(htmlString), cursor=CursorShape.BLOCK, bottom_toolbar=bottom_toolbar)

    def getCity(self):
        city = self.prompt('<skyblue>What city will you begin your adventure in? </skyblue>')
        print_formatted_text(HTML(f'<springgreen>You are living in {city}</springgreen>'))
        return city

    def getName(self):
        name = self.prompt('<skyblue>What is your name? </skyblue>')
        print_formatted_text(HTML(f'<springgreen>Nice to meet you, {name}. Welcome to the WorldEnder.ai augmented reality simulation.</springgreen>'))
        return name

p = Player()

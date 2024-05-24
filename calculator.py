#!/usr/bin/env python
"""
A simple example of a calculator program.
This could be used as inspiration for a REPL.
"""
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import SearchToolbar, TextArea

from player import Player

help_text = """
Welcome to WorldEnder.ai

Enter your name below to get started

Press Control-C to exit.
"""

def main():
    player1 = Player()
    # The layout.

    output_field = TextArea(style="class:output-field", text=help_text)
    status_bar = Window(
        content=FormattedTextControl(player1.statusbar_text),
        style="class:line"
    )
    input_field = TextArea(
        prompt="> ",
        style="class:input-field",
        multiline=False,
        wrap_lines=False,
    )

    game_pane = HSplit(
        [
            output_field,
            input_field
        ]
    )
    container = VSplit(
        [
            game_pane,
            status_bar,
        ]
    )

    starting_prompt = None
    intro = False
    def accept(buff):
        if not player1.name:
            try:
                player1.name = input_field.text
            except BaseException as e:
                output = f"\n\n{e}"
        elif not player1.city:
            try:
                player1.city = input_field.text
            except BaseException as e:
                output = f"\n\n{e}"

        if not player1.name:
            new_text = output_field.text + '\nPlease enter your name below...'
            output_field.buffer.document = Document(
                text=new_text, cursor_position=len(new_text)
            )
        elif not player1.city:
            new_text = output_field.text + '\nPlease enter your starting city below...'
            output_field.buffer.document = Document(
                text=new_text, cursor_position=len(new_text)
            )
        elif not starting_prompt:
            text = 'The WorldEnder.AI interface buzzes and humms as you attach the neural-link interface cable to your spine...'
            output_field.buffer.document = Document(
                text=text, cursor_position=len(text)
            )
        elif intro:
            text = '''
            You wake up in your same old room and feel a sense of dread. Something is not quite right in the world and you can't put your finger on it.

            The whales have attacked.
            '''


    input_field.accept_handler = accept

    # The key bindings.
    kb = KeyBindings()

    @kb.add("c-c")
    @kb.add("c-q")
    def _(event):
        "Pressing Ctrl-Q or Ctrl-C will exit the user interface."
        event.app.exit()

    # Style.
    style = Style(
        [
            ("output-field", "bg:#000044 #ffffff"),
            ("input-field", "bg:#000000 #ffffff"),
            ("line", "bg:#000000 #004400"),
        ]
    )

    # Run application.
    application = Application(
        layout=Layout(container, focused_element=input_field),
        key_bindings=kb,
        style=style,
        mouse_support=True,
        full_screen=True,
    )

    application.run()


if __name__ == "__main__":
    main()

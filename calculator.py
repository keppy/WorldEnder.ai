#!/usr/bin/env python
"""
A simple example of a calculator program.
This could be used as inspiration for a REPL.
"""
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
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
    search_field = SearchToolbar()  # For reverse search.

    output_field = TextArea(style="class:output-field", text=help_text)
    status_bar = Window(
        height=5,
        content=FormattedTextControl(player1.statusbar_text),
        style="class:line"
    )
    input_field = TextArea(
        height=1,
        prompt=">>> ",
        style="class:input-field",
        multiline=False,
        wrap_lines=False,
        search_field=search_field,
    )

    container = HSplit(
        [
            output_field,
            status_bar,
            input_field,
            search_field,
        ]
    )

    def accept(buff):
        if not player1.name:
            try:
                player1.name = input_field.text
            except BaseException as e:
                output = f"\n\n{e}"

        if not player1.name:
            new_text = output_field.text + '\nPlease enter your name below...'
            output_field.buffer.document = Document(
                text=new_text, cursor_position=len(new_text)
            )

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

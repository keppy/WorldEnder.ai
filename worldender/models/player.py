from typing import Any, Dict, List, Optional
from pydantic import BaseModel, computed_field, PrivateAttr
from tabulate import tabulate

DEFAULT_CONFIG: Dict[str, str | int | None] = {
    'name': "",
    'city': "",
    'movement': 10,
    'skill': "Survivalist",
    'item': "Tools",
    'ailment': "",
    'hp': 100,
    'sanity': 100
}

class Player(BaseModel):
    _internal_values: Dict[str, str | int | None] = PrivateAttr(default=DEFAULT_CONFIG)

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self._internal_values = DEFAULT_CONFIG

    @computed_field
    @property
    def city(self) -> str:
        """The city property. A simple string, flexible on what's in it."""
        return self._internal_values['city']

    @city.setter
    def city(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'city'"""
        self._internal_values['city'] = value

    @computed_field
    @property
    def name(self) -> str:
        """The name property. A simple string."""
        return self._internal_values['name']

    @name.setter
    def name(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'name'"""
        self._internal_values['name'] = value

    @computed_field
    @property
    def hp(self) -> int:
        """The hp property. An integer."""
        return self._internal_values['hp']

    @hp.setter
    def hp(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'hp'"""
        self._internal_values['hp'] = value

    @computed_field
    @property
    def sanity(self) -> int:
        """The sanity property. An integer."""
        return self._internal_values['sanity']

    @sanity.setter
    def sanity(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'sanity'"""
        self._internal_values['sanity'] = value

    @computed_field
    @property
    def item(self) -> str:
        """The item property. A string."""
        return self._internal_values['item']

    @item.setter
    def item(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'item'"""
        self._internal_values['item'] = value

    @computed_field
    @property
    def skill(self) -> str:
        """The skill property. A string."""
        return self._internal_values['skill']

    @skill.setter
    def skill(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'skill'"""
        self._internal_values['skill'] = value

    @computed_field
    @property
    def ailment(self) -> str:
        """The ailment property. A string."""
        return self._internal_values['ailment']

    @ailment.setter
    def ailment(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'ailment'"""
        self._internal_values['ailment'] = value

    @computed_field
    @property
    def movement(self) -> str:
        """The movement property. A string."""
        return self._internal_values['movement']

    @movement.setter
    def movement(self, value) -> None:
        """Set the underlying _internal_values dictionary value for 'movement'"""
        self._internal_values['movement'] = value

    def status_table(self) -> str:
        '''Return a table str that shows the player's status in a readable format.'''
        headers = ['property', 'value']
        table = [
            ['Name', self.name],
            ['City', self.city],
            ['Ailment', self.ailment],
            ['HP', self.hp],
            ['Sanity', self.sanity],
            ['Movement', self.movement],
            ['Item', self.item],
            ['Skill', self.skill],

        ]
        table = tabulate(table, headers, tablefmt='rounded_outline')
        return table

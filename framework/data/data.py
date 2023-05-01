"""This module is used for data generation."""
from dataclasses import dataclass


@dataclass
class Person:
    """Data class for person generation."""
    full_name: str = ""
    first_name: str = ""
    last_name: str = ""
    age: int = -1
    salary: int = -1
    department: str = ""
    email: str = ""
    current_address: str = ""
    permanent_address: str = ""
    mobile: str = ""


@dataclass
class Color:
    """Data class for color generation."""
    color_name: list[str] = list[str]

from dataclasses import dataclass


@dataclass
class Person():
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

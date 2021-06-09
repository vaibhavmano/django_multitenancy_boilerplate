from enum import Enum


class UserRole(str, Enum):
    SUPERADMIN = "SUPERADMIN"
    USER = "USER"

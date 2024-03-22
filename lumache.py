"""

Lumache
=======

Utility functions for generating random ingredients and spices.

"""


def get_random_ingredients(kind=None):
    """Returns a list of random ingredients as strings.

    Args:
        kind (list[str]|None): Optional "kind" of ingredients.

    Raises:
        lumache.InvalidKindError: If the kind is invalid.

    Returns:
        list[str]: The ingredients list.
    """
    return ["shells", "gorgonzola", "parsley"]


def get_random_spices(kind=None):
    """
    Return a list of random spices as strings.

    :param kind: Optional "kind" of spices.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The spices list.
    :rtype: list[str]

    """
    return ["pepper", "cumin", "oregano"]


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass

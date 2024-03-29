
def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    def get_generator():
        for element in iterable:
            yield (function_to_apply(element))

    if not hasattr(iterable, '__iter__') or not callable(function_to_apply):
        return None
    return get_generator()

# ... Your code here ...
def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """

    if not hasattr(iterable, '__iter__') or not callable(function_to_apply):
        return None
    res = function_to_apply(iterable[0])
    for i in iterable[1:]:
        res = function_to_apply(res, i)
    return res
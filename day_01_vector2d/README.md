Vector2D
======

Simple Day-1 exercise: implement a small 2D vector class to learn how Python operator
overloading maps to ordinary methods.

Goal
--
Build a `Vector2D` class that implements the following operators and behaviors so you
can see that operator overloading is just method definitions:

- `__add__` — vector addition (Vector2D + Vector2D)
- `__sub__` — vector subtraction (Vector2D - Vector2D)
- `__mul__` — scalar multiplication (Vector2D * number)
- `__eq__` — equality comparison (Vector2D == Vector2D)
- `__repr__` — developer-friendly representation
- `__abs__` — vector magnitude (length)

Expected behavior
--
The class should behave like a small immutable value type. Example usage:

```python
from vector2d import Vector2D

a = Vector2D(1, 2)
b = Vector2D(3, 4)

print(a + b)        # Vector2D(4, 6)
print(a - b)        # Vector2D(-2, -2)
print(a * 3)        # Vector2D(3, 6)
print(a == Vector2D(1, 2))  # True
print(repr(a))      # Vector2D(1, 2)
print(abs(a))       # 2.23606797749979 (sqrt(1^2 + 2^2))
```

Notes
--
- Keep the implementation small and readable; prefer clarity over cleverness.
- `__mul__` here is defined for right-handed scalar multiplication (`v * 3`). If you
	want `3 * v` to work too, implement `__rmul__`.
- Consider adding simple unit tests that assert arithmetic results and `abs()`.

Try it
--
- Open a Python REPL in the project folder and import `Vector2D` to experiment.
- Add a tiny `examples.py` or `tests/test_vector2d.py` if you want automated checks.

Learning outcome
--
By the end you'll understand that expressions like `a + b` are just calls to
`a.__add__(b)`, and that implementing a few dunder methods is enough to make a
type feel like a native numeric type in Python.

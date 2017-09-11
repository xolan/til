# Get exception context

```python
from contextlib import contextmanager

@contextmanager
def error_context():
    try:
        yield
    except Exception as e:
        import pprint
        class CloneException(Exception): pass
        CloneException.__name__ = type(e).__name__
        CloneException.__module___ = type(e).__module__
        message = 'Context: {}'.format(pprint.pformat(error_ctx))
        ce = CloneException(message)
        ce.__traceback__ = e.__traceback__
        raise ce

a = 'herp'
b = 'derp'

with error_context():
    c = a + b
    d = a / b

```

Yields
```
Traceback (most recent call last):
  File "scratch.py", line 6, in with_context
    yield
  File "scratch.py", line 22, in <module>
    d = a / b
TypeError: unsupported operand type(s) for /: 'str' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "scratch.py", line 22, in <module>
    d = a / b
  File "/usr/lib/python3.5/contextlib.py", line 77, in __exit__
    self.gen.throw(type, value, traceback)
  File "scratch.py", line 15, in with_context
    raise ce
  File "scratch.py", line 6, in with_context
    yield
  File "scratch.py", line 22, in <module>
    d = a / b
__main__.TypeError: Context: {'__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'scratch.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4ae2b5c400>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'a': 'herp',
 'b': 'derp',
 'c': 'herpderp',
 'contextmanager': <function contextmanager at 0x7f4ae1339ae8>,
 'error_context': <function error_context at 0x7f4ae1339ea0>}

```

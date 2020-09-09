# Python Cheat Sheet

## Function Decorators

### Plain

```python
def root(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        has_role('root')
        return func(*args, **kwargs)
    return wrapper

@root
def get(self):
    return make_response("ok")
```

### With args

```python
def has_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _has_role(role)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@has_role('admin')
def get(self):
    return make_response("ok")
```

### Both

```python
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

```

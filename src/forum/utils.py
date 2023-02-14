

class _Undefined:

    def __getattr__(self, name) -> str:
        return self

    def __str__(self) -> str:
        return 'null'
    


UNDEFINED = _Undefined()
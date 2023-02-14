from __future__ import annotations
from mysql import connector


class Connection:

    
    def __init__(self) -> None:
        self._conn = connector.connect(option_files = 'database.conf', option_groups = ['connection'])
    

    def __enter__(self) -> Connection:
        return self

    
    def __exit__(self, *exc) -> None:
        self.close()
    
    def execute(self, query: str) -> None:
        self._cursor = self._conn.cursor(dictionary = True)
        self._cursor.execute(query)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()
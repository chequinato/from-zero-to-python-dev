# dir() e help() — Comandos de Exploração do Python

Esses dois comandos servem para **explorar e descobrir** o que existe em qualquer objeto, modulo ou tipo do Python. Use no terminal interativo (`python3`) quando nao lembrar de um metodo ou quiser entender como algo funciona.

---

## dir() — "O que esse objeto tem?"

Mostra todos os metodos e atributos disponiveis de um objeto.

### Uso basico

```python
dir(str)        # mostra tudo que uma string pode fazer
dir(list)       # mostra tudo que uma lista pode fazer
dir(dict)       # mostra tudo que um dicionario pode fazer
```

### Exemplo pratico — dir(str)

```python
>>> dir(str)
['__add__', '__class__', '__contains__', ..., 'capitalize', 'casefold', 'center',
 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### Filtrando so os metodos uteis (sem os dunder `__`)

```python
>>> nome = "Miguel"
>>> [m for m in dir(nome) if not m.startswith("_")]
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust',
 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### dir(list) — metodos uteis

```python
>>> [m for m in dir(list) if not m.startswith("_")]
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
 'reverse', 'sort']
```

### dir(dict) — metodos uteis

```python
>>> [m for m in dir(dict) if not m.startswith("_")]
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
 'setdefault', 'update', 'values']
```

### dir() sem argumento — mostra variaveis no escopo atual

```python
>>> x = 10
>>> lista = [1, 2, 3]
>>> dir()
['__annotations__', '__builtins__', '__doc__', ..., 'lista', 'x']
```

---

## help() — "Como esse metodo funciona?"

Mostra a documentacao detalhada de qualquer funcao, metodo ou modulo.

### Exemplos

```python
>>> help(str.split)
split(self, /, sep=None, maxsplit=-1)
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.
        When set to None (the default value), will split on any whitespace
        character (including \n \r \t \f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits.
        -1 (the default value) means no limit.
```

```python
>>> help(list.append)
append(self, object, /)
    Append object to the end of the list.
```

```python
>>> help(dict.get)
get(self, key, default=None, /)
    Return the value for key if key is in the dictionary, else default.
```

```python
>>> help(len)
len(obj, /)
    Return the number of items in a container.
```

```python
>>> help(print)
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
```

---

## Resumo

| Comando | O que faz | Quando usar |
|---|---|---|
| `dir(objeto)` | Lista metodos e atributos | "O que essa coisa pode fazer?" |
| `dir()` | Lista variaveis no escopo | "O que existe aqui agora?" |
| `help(metodo)` | Mostra documentacao | "Como esse metodo funciona?" |
| `[m for m in dir(x) if not m.startswith("_")]` | Filtra so os uteis | "Quais metodos eu realmente uso?" |

> **Dica:** abra o terminal Python (`python3`) e use `dir()` e `help()` sempre que tiver duvida sobre qualquer coisa. E mais rapido que pesquisar no Google.

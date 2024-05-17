Look through the git log for information.


```bash
git --no-pager log | tail | awk 'NR == 1 { print $2 } '
```

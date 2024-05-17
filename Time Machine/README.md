```bash
git --no-pager log | awk 'NR==5 { print $1 }'
```

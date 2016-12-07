```bash
read -p "Would you something something? " -n 1 -r
echo # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
  # Yes
else
  # No
fi
```

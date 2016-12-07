# Simple Coloring of Strings

```bash
_C_RESET="\e[0m"
_C_RED="\e[31m"
_C_GREEN="\e[32m"
_C_YELLOW="\e[33m"

_I_ERR="${_C_RED}✗  ${_C_RESET}"
_I_OK="${_C_GREEN}✓  ${_C_RESET}"
_I_WAR="${_C_YELLOW}⚠  ${_C_RESET}"

echo -e "${_I_OK}Success!"
echo -e "${_I_ERR}Error!"
echo -e "${_I_WAR}Warning!"
```

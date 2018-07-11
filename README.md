# safepass
Check passwords against https://haveibeenpwned.com/API/v2#PwnedPasswords

## Usage

### For humans

```bash
$ safepass
Password: <enter pwned password (masked)>
NOT SAFE!
$ echo $?
1
$ safepass
Password: <enter not-pwned password (masked)>
SAFE!
$ echo $?
0
```

### For scripting

*Note: scripting mode intended for situations where command history is not saved. Please use above interactive mode if checking directly in command line.*

`$ safepass $PASSWORD`

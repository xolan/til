# TodoTXT Plugin: Sync GDrive

```bash
#!/bin/bash

action=$1
shift

[ "$action" = "usage" ] && {
    echo "    sync"
    echo "      Sync with third party"
    exit
}

[ "$action" = "sync" ] && {
    gdriveExists="`command -v gdrive`"
    tokenFile="${HOME}/.gdrive/token_v2.json"
    if [ ! "${gdriveExists}" ]; then
        echo ">> Could not find command 'gdrive'"
        exit 1
    fi
    if [ ! -f "${tokenFile}" ]; then
        echo ">> Could not find ${tokenFile}"
        echo ">> Please login to GDrive with 'gdrive list'"
        exit 1
    else
        uploadDir="${TODO_DIR}"
        remoteDir=`gdrive list -q "name = '.todo' and trashed = false" --no-header | head -n1 | cut -d " " -f1`
        if [ "${remoteDir}" = "" ]; then
            echo ">> Creating remote directory"
            gdrive mkdir .todo
            echo ">> Restarting"
            $0 sync
        fi
        echo ">> Syncing ${uploadDir} to gdrive:${remoteDir}"
        gdrive sync upload "${uploadDir}" "${remoteDir}"
        exit
    fi
}%
```
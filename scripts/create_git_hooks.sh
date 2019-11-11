#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/../

PRE_PUSH_HOOK="./.git/hooks/pre-push"

if [ -f "$PRE_PUSH_HOOK" ]; then
    echo "$PRE_PUSH_HOOK exist"
else 
    echo "#!/bin/sh" >> $PRE_PUSH_HOOK
    echo "./scripts/test.sh" >> $PRE_PUSH_HOOK
    
    chmod +x $PRE_PUSH_HOOK

    echo "$PRE_PUSH_HOOK created"
fi

#!/bin/bash

#add passphrase to ssh-agent
echo "Please run ssh-agent and ssh-add manually."
echo "ssh-agent bash    // it will open a new bash"
echo "ssh-add"
echo ""
#ssh-agent bash
#ssh-add

echo "Start rsync to clone tc vm to local..."
# clone tc vm direct src to local
#rsync -avzP direct@$1:direct ~/tc_vm
rsync -avzP --delete --exclude-from '/home/stevenfrog/tc_vm/exclude.list' direct@$1:direct ~/tc_vm
# clone tc vm /usr/local/apache/tcdocs to local
#rsync -avzP tc@$1:/mnt/apache/tcdocs ~/tc_vm/apache
# clone tc vm /mnt/shared/web to local
#rsync -avzP --delete --exclude-from '/home/stevenfrog/tc_vm/exclude.list' tc@$1:/mnt/shared/web ~/tc_vm/shared


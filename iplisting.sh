#!/bin/sh


# I took this script from:
# http://www.kalamazoolinux.org/presentations/20010417/list
# and used it and changed it for my own purposes...
# It will probably reside in /usr/sbin

IP_MODULES=`/sbin/lsmod | /usr/bin/gawk '{print $1}' | /bin/grep '^ip'`
if [ "${IP_MODULES}x" = "x" ]; then
   echo You do not have any iptables loaded.
   exit 0
else
   echo You have the following ip modules loaded: ${IP_MODULES}
fi

IPTABLES=/sbin/iptables

echo
echo '                                   FILTER TABLE'
echo
$IPTABLES -t filter -L -n -v --line-numbers
echo
echo '                                   NAT TABLE'
echo
$IPTABLES -t nat -L -v -n --line-numbers
echo
echo '                                  MANGLE TABLE'
echo '                                   was ignored'     

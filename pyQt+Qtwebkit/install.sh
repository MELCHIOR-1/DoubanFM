#!/bin/sh
myName=`stat -c %U $0`
homeDir=/home/${myName}
setupFolder=${homeDir}/Music/DoubanFM
echo "myname=${myName}"
echo "homeDir=${homeDir}"
echo "setupFolder=${setupFolder}"
if [ ! -d ${setupFolder} ]; then
  mkdir -vp -m 777 ${setupFolder}
  chown ${myName} ${setupFolder}
fi
echo ${homeDir}
cp -fpv douban* ${setupFolder}
echo "cd ${setupFolder}\npython doubanFM.py" > ${setupFolder}/doubanFM.sh
echo "[Desktop Entry]\nName=doubanFM\nIcon=${setupFolder}/douban.png\nExec=sh ${setupFolder}/doubanFM.sh\nStartupNotify=true\nTerminal=false\nType=Application\nCategories=Network;fm;\nTargetEnvironment=Unity" > ${setupFolder}/doubanFM.desktop
chown ${myName} ${setupFolder}/doubanFM.desktop
chmod 777 ${setupFolder}/*
cp -fpv ${setupFolder}/doubanFM.desktop /usr/share/applications/


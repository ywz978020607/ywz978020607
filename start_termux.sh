nginx
cd src/
uwsgi --ini django1/uwsgi.ini
crond start
sshd
cd /data/data/com.termux/files/home/syncthing-linux-arm64-v1.23.1/
./syncthing &

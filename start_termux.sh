nginx
cd docker_nginx_with_manage/
uwsgi --ini django1/uwsgi.ini
cd /root/server_dockers/frpc
./frpc_linux_amd64 -c frpc.ini &
crond start
sshd
cd /data/data/com.termux/files/home/syncthing-linux-arm64-v1.23.1/
./syncthing &

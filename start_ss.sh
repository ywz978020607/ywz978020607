cd /root/docker_nginx_with_manage/docker
docker-compose up -d
cd /root/server_dockers/frpc
./frpc_linux_amd64 -c frpc.ini &
cd /root/server_dockers/nextcloud
docker-compose up -d
cd /root/server_dockers/
bash wangxin.sh
# emby, syncthing are services

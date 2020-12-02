# Docker Applications

* **Nginx SPA**

> An dockerized server to serve local docs and spa  
> [more](./nginx_spa.md)

* **rtmp server**

> docker rtmp server  
> `docker run -d -p 1935:1935 --name rtmp tiangolo/nginx-rtmp`

* **FTP Server**

> docker ftp server  
> `docker run -d -v ~/share:/home/vsftpd -p 20:20 -p 21:21 -p 47400-47470:47400-47470 -e FTP_USER=user -e FTP_PASS=password -e PASV_ADDRESS=ip_addr --name ftp --restart=always bogem/ftp`

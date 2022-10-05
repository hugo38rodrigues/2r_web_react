## Apache deployment

### Host react application on Apache server

source : https://gist.github.com/ywwwtseng/63c36ccb58a25a09f7096bbb602ac1de

Récupérer le fichier `my-httpd.conf` à partir de celui de l'image httpd:

```bash
docker run --rm httpd:2.4 cat /usr/local/apache2/conf/httpd.conf > my-httpd.conf
```

Configurer le fichier `my-httpd.conf` avec les paramètres suivant :

```bash
<Directory "/usr/local/apache2/htdocs">
    #
    # Possible values for the Options directive are "None", "All",
    # or any combination of:
    #   Indexes Includes FollowSymLinks SymLinksifOwnerMatch ExecCGI MultiViews
    #
    # Note that "MultiViews" must be named *explicitly* --- "Options All"
    # doesn't give it to you.
    #
    # The Options directive is both complicated and important.  Please see
    # http://httpd.apache.org/docs/2.4/mod/core.html#options
    # for more information.
    #
    Options Indexes FollowSymLinks

    #
    # AllowOverride controls what directives may be placed in .htaccess files.
    # It can be "All", "None", or any combination of the keywords:
    #   Options FileInfo AuthConfig Limit
    #
    AllowOverride All

    Options -MultiViews
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.html [QSA,L]

    #
    # Controls who can get stuff from this server.
    #
    Require all granted
</Directory>
```

### Configuration SSL du serveur Apache

source : https://hub.docker.com/_/httpd

Créer d'un certificat auto-signé à placer dans les répertoires suivant :

- ~/server/cert/certs/apache-selfsigned.crt
- ~/server/cert/private/apache-selfsigned.key

via openssl :

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/server/cert/private/apache-selfsigned.key -out ~/server/cert/certs/apache-selfsigned.crt
```

Créer un fichier `my-httpd.conf` à partir de celui de l'image httpd:

```bash
docker run --rm httpd:2.4 cat /usr/local/apache2/conf/httpd.conf > my-httpd.conf
```

Créer un fichier `my-httpd-ssl.conf` à partir de celui de l'image httpd:

```bash
docker run --rm httpd:2.4 cat /usr/local/apache2/conf/extra/httpd-ssl.conf > my-httpd-ssl.conf
```

Activer les modules Apache pour faire du https dans le fichier `my-httpd.conf`

```
LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
LoadModule ssl_module modules/mod_ssl.so
LoadModule rewrite_module modules/mod_rewrite.so
Include conf/extra/httpd-ssl.conf
```

### Build apache image

```bash
docker build -t apache_2r .
```

### Deploy Apache server with frontend

```bash
docker run --name apache_2r  -v /media/xwdrblue/Disque/projet_2r/server/cert:/etc/ssl -p 443:443 apache_2r
```

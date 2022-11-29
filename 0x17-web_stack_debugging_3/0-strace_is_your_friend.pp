# Debugs apache2 server error

exec { 'mv /var/www/html/readme.html /var/www/html/index.html':
  path => '/usr/bin:/usr/sbin:/bin'
}

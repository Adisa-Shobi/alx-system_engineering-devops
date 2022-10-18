# Installs and configures an nginx server
include stdlib

package { 'nginx':
  provider => 'apt',
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
}

file_line { 'server_name _;':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  line   => "server_name _;\n\trewrite ^/redirect_me(.*)$ http://www.youtube.com\
 permanent$1;\n\terror_page 404 /custom_404.html;\n\tlocation \
= /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;",
  match  => 'server_name _;',
}

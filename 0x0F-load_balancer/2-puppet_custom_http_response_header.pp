# Configures nginx server by adding custom headers

exec {'install nginx':
  command => 'apt-get -y update;sudo apt-get -y install nginx',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

exec {'restore permissions':
  command => 'sudo sed -i "/listen 80 default_server;/a add_header     X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default;',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

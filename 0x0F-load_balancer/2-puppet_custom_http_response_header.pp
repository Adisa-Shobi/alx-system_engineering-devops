# Configures nginx server by adding custom headers

exec {'install nginx':
  command => 'apt-get update;sudo apt-get -y install nginx',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

exec {'change permissions':
  command => 'sudo chown $USER:$USER /etc/nginx/sites-available/default',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\tadd_header X-Served-By \$hostname;\n\trewrite ^/redirect_me(.*)$ http://www.youtube.com/ permanent;\n}\n",
}

exec {'restore permissions':
  command => 'sudo chown root:root /etc/nginx/sites-available/default',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin'
}

# Fixing failed requests errors

exec { 'lets try increasing th number of workers':
  command => 'sudo sed -i "s/14096/" /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin:/bin:/sbin',
}


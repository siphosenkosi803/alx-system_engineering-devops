# new fix

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# Adjusting NGINX worker_processes and worker_connections\n\
              worker_processes auto;\n\
              events {\n\
                worker_connections 100;\n\
              };\n",
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}

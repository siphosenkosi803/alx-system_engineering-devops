# Fixing failed requests errors

file { '/path/to/custom/nginx.conf':
  ensure  => file,
  owner   => 'user',
  group   => 'group',
  mode    => '0644',
  content => "worker_processes auto;\n\
              events { worker_connections 100; };\n",
} -> exec { 'lets restart nginx now':
  command     => 'service nginx restart',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure => 'present',
}

file_line { 'http_header':
  path  => '/etc/nginx/sites-available/default',
  match => 'server {',
  line  => "server {\n\tadd_header X-Served-By \"${hostname}\";\n",
}

exec {'run':
  command => '/usr/sbin/service nginx restart',
}

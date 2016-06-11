# Flea_Market

=== apache configuration ===

LoadModule cgi_module /usr/lib/apache2/modules/mod_cgi.so

Alias /market /opt/web/market

<Directory /opt/web/market>
    
    Order allow,deny
    Allow from all
    Require all granted
    
#    AllowOverride None
    Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
    AddHandler cgi-script .cgi .pl

</Directory>

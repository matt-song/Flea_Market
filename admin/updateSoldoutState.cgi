#!/usr/bin/perl
use strict;
use Data::Dumper;
use CGI;
use CGI::Session;
use lib '/opt/web/market/lib/';
use MARKET;

my $cgi = CGI->new;
print $cgi->header;
print $cgi->start_html( -title=>'EMC Flea Market Report',
#        -style=>{-src=>'/market/css/admin.css'}
);

# Get POST value
my $Form_id = $cgi->param("id");
my $Form_soldout = $cgi->param("dSoldOut");

if ( ("x$Form_id" eq 'x') ||( "x$Form_soldout" eq 'x' ) )
{
    print qq(<h4>DB entries:</h4>\n);
    my $output = MARKET->executeSQL("select * from Donation");
    MARKET->print_DEBUG($output);

    print qq(<h4>Input the setting you would like to change: </h4>\n);
    print qq(
    <form name="updateSoldoutState" action="/market/admin/updateSoldoutState.cgi" method="POST">
        <input type="text" name="id" id="id" placeholder="input the id of entry" />
        <select name="dSoldOut">
            <option value="0" selected="selected">no</option>
            <option value="1">yes</option>
        </select>   
    <p>
        <input type="submit" value="submit" />
    </p>
    </form>
)
}
else
{
    my $output = MARKET->executeSQL("update Donation set soldOut=$Form_soldout where id=$Form_id;");
    print qq(<font size="4" color="Green">Update successful, Set id [$Form_id]'s soldout state to [$Form_soldout] </font>)  if ("x$output" eq 'x');
    print qq(<p><a href="/market/admin/updateSoldoutState.cgi">Back</a></p>)
}

print $cgi->end_html;

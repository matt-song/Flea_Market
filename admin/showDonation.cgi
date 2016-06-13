#!/usr/bin/perl
use strict;
use Data::Dumper;
use CGI;
use CGI::Session;
use lib '/opt/web/market/lib/';
use MARKET;

my $DEBUG = 0; 
my $upload_folder = '/opt/web/market/upload';
my $ImgURLPath = '/market/upload/';
my $defaultImage = '/market/img/pictureIsMissing.png';


my $cgi = CGI->new;
print $cgi->header;

print $cgi->start_html( -title=>'EMC Flea Market Report',
        -style=>{-src=>'/market/css/admin.css'}
);
print qq(<link rel="stylesheet" href="/market/css/normalize.css">);

my $output = MARKET->executeSQL("select * from Donation");
MARKET->print_DEBUG($output) if $DEBUG;

print qq(
    <div class="Donation-Table">
        <div class="header">EMC Flea Market Report</div>
        
            <table cellspacing="0">
                <tr>
                    <th>UID</th>
                    <th>User Name</th>
                    <th>Goods Name</th>
                    <th>Category</th>
                    <th>Price</th>
                    <th>Image</th>
                </tr>
);

foreach my $entry (split(/^/,$output))
{
    my ($uID,$uName,$dName,$dCategory,$dPrice,$dImageName) = split(/\|/,$entry);
    # MARKET->print_DEBUG("$uID $uName $dName $dCategory $dImageName");
    
    my $imageURL = "$ImgURLPath/$dImageName";
    my $Category = MARKET->getCategoryByID($dCategory);

    print qq(
                <tr>
                    <td>$uID</td>
                    <td>$uName</td>
                    <td>$dName</td>
                    <td>$Category</td>
                    <td>$dPrice</td>
                    <td><a href="$imageURL"><img src="$imageURL" style="width:200px;height:150px;" /></a></td>
                </tr>
);
}

print qq(
            </table>
        </div>
    </div>

</body>
</html>
);

print $cgi->end_html;


#!/usr/bin/perl
use strict;
use Data::Dumper;
use CGI;
use CGI::Session;
use lib '/opt/web/market/lib/';
use MARKET;
#use Encode;

my $DEBUG = 1; 

my $cgi = CGI->new;
print $cgi->header;
#print $cgi->header(-charset=>'utf-8');

# Define the parameter from form
my ($Form_uName, $Form_uID, $Form_dName, $Form_dImage, $uploadfilehandle);

# Get the value from form
foreach my $param ($cgi->param())
{
    $Form_uName = $cgi->param($param) if ($param eq "uName");
    $Form_uID = $cgi->param($param) if ($param eq "uID");
    $Form_dName = $cgi->param($param) if ($param eq "dName");
    $Form_dImage = $cgi->param($param) if ($param eq "dImage");
    $uploadfilehandle = $cgi->upload("dImage") if ($param eq "dImage");
}

MARKET->print_DEBUG("User Name: [$Form_uName]\nUID: [$Form_uID]\nGood Name: [$Form_dName]\nImage: [$Form_dImage]") if ($DEBUG);
MARKET->print_DEBUG("file handle is [$uploadfilehandle]");

open UPLOADFILE,">./$Form_dImage"; 
binmode UPLOADFILE; 

while ( <$uploadfilehandle> )
{
    print UPLOADFILE; 
} 

 

# check if any input is missing
# tbd

print $cgi->end_html;

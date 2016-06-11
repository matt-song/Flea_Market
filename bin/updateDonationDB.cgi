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
    #$uploadfilehandle = $cgi->upload("dImage") if ($param eq "dImage");
}

my $upload_filehandle = $cgi->upload("dImage");

open ( UPLOADFILE, ">/tmp/image_test.jpg" ) or die "$!";
binmode UPLOADFILE;

while ( <$upload_filehandle> )
{
    print UPLOADFILE;
}

close UPLOADFILE;


#open ( IMAGE,'>','/tmp/image.jpg' );
#while ( my $bytesread = $io_handle->read($buffer,1024) ) {
#    print $out_file $buffer;
#}


MARKET->print_DEBUG("User Name: [$Form_uName]\nUID: [$Form_uID]\nGood Name: [$Form_dName]\nImage: [$Form_dImage]") if ($DEBUG);
MARKET->print_DEBUG("file handle is [$uploadfilehandle]");

# print Dumper $cgi->param();
# $VAR1 = 'uName'; $VAR2 = 'uID'; $VAR3 = 'dName'; $VAR4 = 'dImage';


 

# check if any input is missing
# tbd

print $cgi->end_html;

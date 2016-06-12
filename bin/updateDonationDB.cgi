#!/usr/bin/perl
use strict;
use Data::Dumper;
use CGI;
use CGI::Session;
use lib '/opt/web/market/lib/';
use MARKET;

my $DEBUG = 1; 
my $upload_folder = '/opt/web/market/img';

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
}

# print debug message
MARKET->print_DEBUG("User Name: [$Form_uName]\nUID: [$Form_uID]\nGood Name: [$Form_dName]\nImage: [$Form_dImage]") if ($DEBUG);
MARKET->print_DEBUG("file handle is [$uploadfilehandle]");

# check if any value is missing
MARKET->print_ERROR("Missing value, please check the form and sumbit again!") if ((!$Form_uName)||(!$Form_uID)||(!$Form_dName)||(!$Form_dImage));

# upload the image
uploadFile();

sub uploadFile
{
    my $upload_filehandle = $cgi->upload("dImage");
    print Dumper $upload_filehandle;
    
    open ( UPLOADFILE, ">$upload_folder/$Form_dImage" ) or die "$!";
    binmode UPLOADFILE;
    while ( <$upload_filehandle> )
    {
        print UPLOADFILE;
    }
    close UPLOADFILE;
    return 0;
}


 


print $cgi->end_html;

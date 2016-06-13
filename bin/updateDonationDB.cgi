#!/usr/bin/perl
use strict;
use Data::Dumper;
use CGI;
use CGI::Session;
use lib '/opt/web/market/lib/';
use MARKET;

my $DEBUG = 1; 
my $upload_folder = '/opt/web/market/upload';

my $cgi = CGI->new;
print $cgi->header;
#print $cgi->header(-charset=>'utf-8');

# Get POST value
my $Form_uName = $cgi->param("uName");
my $Form_uID = $cgi->param("uID");
my $Form_dName = $cgi->param("dName");
my $Form_dCategory = $cgi->param("dCategory");
my $Form_dImage = $cgi->param("dImage");

# print debug message
MARKET->print_DEBUG("User Name: [$Form_uName]\nUID: [$Form_uID]\nGood Name: [$Form_dName]\nCategroy: [$Form_dCategory]\nImage: [$Form_dImage]") if ($DEBUG);

# check if any value is missing
if ((!$Form_uName)||(!$Form_uID)||(!$Form_dName)||(!$Form_dImage)) 
{
    MARKET->print_ERROR("Missing value, please check the form and sumbit again!");
    print $cgi->end_html;
    exit 1;
}

# upload the image
my $uploadImageName = uploadFile($Form_uID);

# update the DB
MARKET->updateDonationDB($Form_uID, $Form_uName, $Form_dName, $Form_dCategory, $uploadImageName);


sub uploadFile
{
    my $uid = shift;
   
    chomp(my $timeStamp = `date +%s`);
    my $fileName = "image_${uid}_${timeStamp}";
    MARKET->print_DEBUG("The uploaded file name is [$fileName]") if ($DEBUG);
    
    my $upload_filehandle = $cgi->upload("dImage");
    open ( UPLOADFILE, ">$upload_folder/$fileName" ) or do { MARKET->print_ERROR("Failed to upload files"); exit 1;};
    binmode UPLOADFILE;
    while ( <$upload_filehandle> )
    {
        print UPLOADFILE;
    }
    close UPLOADFILE;
    return $fileName;
}

print $cgi->end_html;

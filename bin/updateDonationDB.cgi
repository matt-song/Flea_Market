#!/usr/bin/perl
use strict;
use Data::Dumper;
use CGI;
use CGI::Session;
use lib '/opt/web/market/lib/';
use MARKET;

my $DEBUG = 0; 
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
errorOut("Missing value, please check the form and sumbit again!") if ((!$Form_uName)||(!$Form_uID)||(!$Form_dName)||(!$Form_dImage));

# check if we have any invalid input, if so, return a error message
if ($Form_uName !~ /^[\w\s]+$/)
{
    errorOut("Invalid user name [$Form_uName], must be [a-z, 0-9]");
}
elsif ($Form_uID !~ /^\d+$/)
{
    errorOut("Invalid User ID [$Form_uID], must be [0-9]");
}
elsif ($Form_dName !~ /^[\w\s]+$/)
{
    errorOut("Invalid donation name [$Form_dName], must be [a-z, 0-9]");
}

# upload the image
my $uploadImageName = uploadFile($Form_uID);

# update the DB
MARKET->updateDonationDB($Form_uID, $Form_uName, $Form_dName, $Form_dCategory, $uploadImageName);

# print thanks page if submit successful
print qq(<font size="4" color="Green">Upload successful, thank you!</font>\n);
print qq(<p><a href="/market/formUpdate.html">Back</a></p>);

sub errorOut
{
    my $message = shift;
    MARKET->print_ERROR($message);
    print $cgi->end_html;
    exit 1;
}

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


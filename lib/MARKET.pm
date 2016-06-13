#!/usr/bin/perl
package MARKET;
use strict;
use Data::Dumper;
use CGI;

my $DEBUG = 0;
my $DB = "/opt/web/market/db/market.db";

## print the debug message.
sub print_DEBUG
{
    my ($self, $message) = @_;
    print "<pre>\n$message\n</pre>\n";    
    return 0;
}

sub print_ERROR
{
    my ($self, $message) = @_;
    print qq(<font size="4" color="red">$message</font>\n);    
    return 0;
}

### update the Donation table
sub updateDonationDB
{
    my ($self, $uid, $uName, $dName, $dCategory, $imageName) = @_;

    my $sqlCMD = qq(INSERT INTO Donation VALUES ('$uid','$uName','$dName','$dCategory','$imageName'););
    print_DEBUG('self', "the sql command is [$sqlCMD]") if $DEBUG;

    &executeSQL('self', $sqlCMD);
}

### common function for execute SQL command
sub executeSQL
{
    my ($self, $sqlCMD) = @_;
   
    my $bashCMD = qq(sqlite $DB "$sqlCMD" 2>&1);
    print_DEBUG('self',"the bash command is [$bashCMD]") if $DEBUG;
    
    chomp(my $output = `$bashCMD`);
    
    if ($?)
    {
        print_ERROR('self', "Failed to update DB with command [$sqlCMD], error [$output], please check!");
        return 1;
    }
    else
    {
        return $output;
    }

}


1;

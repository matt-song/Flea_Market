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

my $output = MARKET->executeSQL("select * from Donation");
MARKET->print_DEBUG($output);

print $cgi->end_html;

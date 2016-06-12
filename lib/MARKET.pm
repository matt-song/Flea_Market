#!/usr/bin/perl
package MARKET;
use strict;
use Data::Dumper;
use CGI;

## print the debug message.
sub print_DEBUG
{
    my ($self, $message) = @_;
    print "<pre> $message </pre>\n";    
    return 0;
}

sub print_ERROR
{
    my ($self, $message) = @_;
    print qq(<font size="4" color="red">$message</font>\n);    
    return 0;
}

1;

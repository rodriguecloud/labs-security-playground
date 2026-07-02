#!/usr/bin/perl
use strict;
use warnings;

print "Enter the host address to ping: ";
my $host = <STDIN>;
chomp($host);

# VULNERABILITY: The string is passed directly to the shell.
# An attacker can terminate the ping command and start a new one.
# Malicious input example: "8.8.8.8; cat /etc/passwd"
my $command = "ping -c 1 " . $host;

print "Executing: $command\n";
system($command);

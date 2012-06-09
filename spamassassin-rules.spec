Summary:	Rules for SpamAssassin
Name:		spamassassin-rules
Version:	3.3.2
Release:	0.20120609.1
License:	Apache License
Group:		Networking/Mail
URL:		http://spamassassin.org/
Requires:	spamassassin > 3.3.0
Conflicts:	spamassassin < 3.3.0
Buildrequires:	spamassassin
Buildrequires:	gnupg
Buildrequires:	perl(Digest::SHA1)
Buildrequires:	perl(HTML::Parser)
Buildrequires:	perl(Net::DNS)
Buildrequires:	perl(NetAddr::IP)
Buildrequires:	perl(Time::HiRes)
Buildrequires:	perl(Archive::Tar)
Buildrequires:	perl(IO::Zlib)
Buildrequires:	perl(Digest::SHA1)
Buildrequires:	perl(MIME::Base64)
Buildrequires:	perl(DB_File)
Buildrequires:	perl(Net::SMTP)
Buildrequires:	perl(Mail::SPF)
Buildrequires:	perl(IP::Country::Fast)
Buildrequires:	perl(Razor2::Client::Agent)
Buildrequires:	perl(Net::Ident)
Buildrequires:	perl(IO::Socket::INET6)
Buildrequires:	perl(IO::Socket::SSL)
Buildrequires:	perl(Compress::Zlib)
Buildrequires:	perl(Mail::DKIM)
Buildrequires:	perl(DBI)
Buildrequires:	perl(Getopt::Long)
Buildrequires:	perl(LWP::UserAgent)
Buildrequires:	perl(HTTP::Date)
Buildrequires:	perl(Encode::Detect)
BuildArch:	noarch

%description
This package contains the default rules for SpamAssassin.

WARNING: These rules may be old at install time. This package is NOT
supported by Mandriva. You should immediately update your rules set as
explained in the official SpamAssassin documentations.

%prep

%setup -q -c -T -n %{name}-%{version}
sa-update --debug --gpghomedir . --channel updates.spamassassin.org --updatedir .

%build

%install

install -d %{buildroot}%{_datadir}/spamassassin
install -m0644 updates_spamassassin_org/*.cf %{buildroot}%{_datadir}/spamassassin

%files
%attr(0644,root,root) %{_datadir}/spamassassin/*.cf

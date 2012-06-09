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

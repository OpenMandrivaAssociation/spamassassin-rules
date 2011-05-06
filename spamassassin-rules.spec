Summary:	Rules for SpamAssassin
Name:		spamassassin-rules
Version:	3.3.1
Release:	%mkrel 0.20101015.2
License:	Apache License
Group:		Networking/Mail
URL:		http://spamassassin.org/
Requires:	spamassassin > 3.3.0
Conflicts:	spamassassin < 3.3.0
Buildrequires:	spamassassin
Buildrequires:	gnupg
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains the default rules for SpamAssassin.

WARNING: These rules may be old at install time. This package is NOT
supported by Mandriva. You should immediately update your rules set as
explained in the official SpamAssassin documentations.

%prep

%setup -q -c -T -n %{name}-%{version}
sa-update --gpghomedir . --channel updates.spamassassin.org --updatedir .

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/spamassassin
install -m0644 updates_spamassassin_org/*.cf %{buildroot}%{_datadir}/spamassassin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0644,root,root) %{_datadir}/spamassassin/*.cf

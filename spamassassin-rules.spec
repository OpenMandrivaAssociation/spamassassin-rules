%define svn_ver r1840640
Summary:	Rules for SpamAssassin
Name:		spamassassin-rules
Version:	3.4.2
Release:	1.%{svn_ver}
License:	Apache License
Group:		Networking/Mail
URL:		http://spamassassin.apache.org/
Requires:	spamassassin >= 3.4.0
Conflicts:	spamassassin < 3.4.0
Source0:	Mail-SpamAssassin-rules-%{version}.%{svn_ver}.tgz
BuildRequires:	spamassassin >= 3.4.0
BuildRequires:	gnupg
BuildArch:	noarch

%description
This package contains the default rules for SpamAssassin.

WARNING: These rules may be old at install time. This package is NOT
supported by Mandriva. You should immediately update your rules set as
explained in the official SpamAssassin documentations.

%prep

%setup -q -c -n %{name}-%{version}

%build

%install

install -d %{buildroot}%{_datadir}/spamassassin
install -m0644 *.cf %{buildroot}%{_datadir}/spamassassin

%files
%defattr(-,root,root)
%attr(0644,root,root) %{_datadir}/spamassassin/*.cf

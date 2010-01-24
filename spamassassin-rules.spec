%define fname Mail-SpamAssassin-rules

Summary:	Rules for SpamAssassin
Name:		spamassassin-rules
Version:	3.3.0
Release:	%mkrel 0.1
License:	Apache License
Group:		Networking/Mail
URL:		http://spamassassin.org/
Source0:	http://www.apache.org/dist/spamassassin/source/%{fname}-%{version}.tgz
Source1:	http://www.apache.org/dist/spamassassin/source/%{fname}-%{version}.tgz.asc
Requires:	spamassassin >= 3.3.0
Conflicts:	spamassassin < 3.3.0
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains the default rules for SpamAssassin.

%prep

%setup -q -c -T -n %{fname}-%{version} -a0

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/spamassassin
install -m0644 *.cf %{buildroot}%{_datadir}/spamassassin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0644,root,root) %{_datadir}/spamassassin/*.cf


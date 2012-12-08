Summary:	Rules for SpamAssassin
Name:		spamassassin-rules
Version:	3.3.2
Release:	%mkrel 0.20110530.2
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


%changelog
* Mon May 30 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.2-0.20110530.1mdv2011.0
+ Revision: 681793
- bump version and release

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.1-0.20101015.2
+ Revision: 670006
- mass rebuild

* Fri Oct 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.1-0.20101015.1mdv2011.0
+ Revision: 585786
- ahh, use sa-update instead...

* Fri Oct 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.1-0.1.r923257.1mdv2011.0
+ Revision: 585776
- only slightly newer rules. (r923257)

* Sun Aug 01 2010 Thomas Spuhler <tspuhler@mandriva.org> 3.3.1-0.1.r923114.2mdv2011.0
+ Revision: 564162
- Increased release for rebuild

  + Luis Daniel Lucio Quiroz <dlucio@mandriva.org>
    - fix requires to warant SA sintax
    - Update to snap 923114

* Wed Apr 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-0.1.r901671.2mdv2010.1
+ Revision: 540449
- add a disclamier of liability, somewhat...

* Sun Jan 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-0.1.r901671.1mdv2010.1
+ Revision: 495502
- use newer rules, 3.3.0 was quite old...

* Sun Jan 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-0.1mdv2010.1
+ Revision: 495487
- import spamassassin-rules


* Sun Jan 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-0.1mdv2010.0
- initial Mandriva package

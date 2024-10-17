Summary:	Tool to determine the ink levels of HP and Epson inkjets
Name:		ink
Version:	0.5.1
Release:	2
License:	GPLv3
Group:		Publishing
Url:		https://ink.sourceforge.net/
BuildRequires:  libinklevel-devel >= 0.8.0
Source:		http://heanet.dl.sourceforge.net/sourceforge/ink/%{name}-%{version}.tar.gz
Patch0:		ink-0.5.1-fix-str-fmt.patch

%description
ink is a command line tool for checking the ink level of your printer on
a system which runs Linux. It supports printers attached via parallel
port or usb.

Most current HP inkjets and several Epson inkjets are supported.

Note that ink only works when the printer is not printing and when the
printer port is not occupied by HPOJ.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make CFLAGS="%{optflags}"

%install
# Remove explicit setting of ownerships from the Makefile
perl -p -i -e 's/-o root -g root//' Makefile

%makeinstall_std PREFIX=%{_prefix}


%files
%doc COPYING README
# This should run SGID sys, so that it can access the printer device files
# when started by a normal user
%attr(2755,lp,sys) %{_bindir}/*
%{_mandir}/man1/ink.1.*



%changelog
* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.5.1-1mdv2010.1
+ Revision: 515754
- clean spec
- use configure2_5x
- drop old patch
- update to 0.5.1
- add a new patch for fix string format

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 335695
- fix linkage
- New version 0.5.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-3mdv2009.0
+ Revision: 247230
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 165961
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 09 2007 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2008.0
+ Revision: 50588
- New version


* Wed Apr 05 2006 Lenny Cartier <lenny@mandriva.com> 0.3.1-1mdk
- 0.3.1

* Sun Nov 28 2004 Till Kamppeter <till@mandrakesoft.com> 0.3-1mdk
- Updated to version 0.3.
- New URL.


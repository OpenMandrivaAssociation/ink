Summary:	Tool to determine the ink levels of HP and Epson inkjets
Name:		ink
Version:	0.5.1
Release:	%mkrel 1
License:	GPLv3
Group:		Publishing
Url:		http://ink.sourceforge.net/
BuildRequires:  libinklevel-devel >= 0.8.0
Source:		http://heanet.dl.sourceforge.net/sourceforge/ink/%{name}-%{version}.tar.gz
#Patch0 sent upstream by Kharec
Patch0:		ink-0.5.1-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
rm -rf $RPM_BUILD_ROOT

# Remove explicit setting of ownerships from the Makefile
perl -p -i -e 's/-o root -g root//' Makefile

%makeinstall_std PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
# This should run SGID sys, so that it can access the printer device files
# when started by a normal user
%attr(2755,lp,sys) %{_bindir}/*
%{_mandir}/man1/ink.1.lzma


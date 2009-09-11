##### GENERAL STUFF #####

Summary:	Tool to determine the ink levels of HP and Epson inkjets
Name:		ink
Version:	0.5.0
Release:	%mkrel 2
License:	GPL
Group:		Publishing
Url:		http://ink.sourceforge.net/
BuildRequires:  libinklevel-devel >= 0.8.0

##### SOURCE FILES #####

Source: http://heanet.dl.sourceforge.net/sourceforge/ink/%{name}-%{version}.tar.gz
Patch0: ink-0.5.0-fix-str-fmt.patch
Patch1: ink-0.5.0-linkage.patch

##### ADDITIONAL DEFINITIONS #####

BuildRoot:	%{_tmppath}/%{name}-buildroot

##### DESCRIPTION #####

%description
ink is a command line tool for checking the ink level of your printer on
a system which runs Linux. It supports printers attached via parallel
port or usb.

Most current HP inkjets and several Epson inkjets are supported.

Note that ink only works when the printer is not printing and when the
printer port is not occupied by HPOJ.


##### PREP #####

%prep
%setup -q
%patch0 -p0
%patch1 -p0

##### BUILD #####

%build
%make CFLAGS="%{optflags}"

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

# Remove explicit setting of ownerships from the Makefile
perl -p -i -e 's/-o root -g root//' Makefile

%makeinstall_std PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT


##### FILE LIST #####

%files
%defattr(-,root,root)
%doc COPYING README
# This should run SGID sys, so that it can access the printer device files
# when started by a normal user
%attr(2755,lp,sys) %{_bindir}/*

##### CHANGELOG #####

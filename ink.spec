##### GENERAL STUFF #####

Summary:	Tool to determine the ink levels of HP and Epson inkjets
Name:		ink
Version:	0.3.1
Release:	%mkrel 1
License:	GPL
Group:		Publishing
Url:		http://ink.sourceforge.net/
BuildRequires:  libinklevel-devel

##### SOURCE FILES #####

Source: http://heanet.dl.sourceforge.net/sourceforge/ink/%{name}-%{version}.tar.bz2

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
rm -rf $RPM_BUILD_DIR/ink
%setup -q -n ink

##### BUILD #####

%build
%make

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

# Remove explicit setting of ownerships from the Makefile
perl -p -i -e 's/-o root -g root//' Makefile

%makeinstall DESTDIR=%{buildroot}/usr

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


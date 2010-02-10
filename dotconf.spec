Summary: dot.conf
Name: dotconf
Version: 1.1.0
Release: 1
Copyright: LGPL
Group: Development/Libraries
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
Packager: Benjamin Lee <benjamin.lee@dotwap.com>

%description
dotconf is a configuration file parser.

%prep
rm -rf $RPM_BUILD_ROOT

%setup
%build
./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
# %doc README README.docbook README.src README.wmlscript INSTALL AUTHORS COPYING VERSION NEWS ChangeLog doc/ gw/control.html contrib/

%{_prefix}/lib/libpool.a
%{_prefix}/lib/libdotconf*.so*
%{_prefix}/lib/libdotconf.la
%{_prefix}/lib/libdotconf.a
%{_prefix}/include/libpool.h
%{_prefix}/include/dotconf.h
%{_prefix}/bin/dotconf-config
%{_prefix}/share/aclocal/dotconf.m4

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%changelog
* Fri Apr 05 2002 Mike Javorski <mike_javorski@bigfoot.com>
- Fixed inclusion of .so files
* Mon Dec 24 2001 Benjamin Lee <benjamin.lee@dotwap.com>
- initial release of dotconf rpm package.

%global debug_package ${nil}

%define __python3 /usr/bin/python3.8

Name:           python3-dateutils
Version:        0.6.12
Release:        0
Summary:        dateutils package
Group:          Application/Network
License:        GPL
URL:            https://github.com/jmcantrell/python-dateutils
Vendor:         jmcantrell
Source:         packagesource.tar.gz
Prefix:         %{_prefix}
Packager:       Dragonfly
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      x86_64
BuildRequires:  python38-devel, python38
Requires:       python38

%description
dateutils middleware

%prep
%setup -c .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root %{buildroot}

%check
%{__python3} setup.py test

%files
%{python3_sitelib}/*
%{_bindir}/dateadd
%{_bindir}/datediff

%changelog
* Wed Oct 05 2022 Dragonfly <dragonfly@upnext.com> - 0.6.12-0
- First package dateutils


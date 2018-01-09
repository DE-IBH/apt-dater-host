Name:           apt-dater-host
Version:        1.0.1
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Host helper application for apt-dater

License:        GPL2
URL:            https://github.com/DE-IBH/apt-dater-host/
Source0:        https://github.com/DE-IBH/apt-dater-host/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Host helper application for apt-dater, a terminal-based remote package update
manager. apt-dater provides an easy to use ncurses frontend for managing package
updates on a large number of remote hosts using SSH.  It supports Debian-based
managed hosts as well as OpenSUSE and CentOS based systems.

%prep
%autosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
install yum/apt-dater-host $RPM_BUILD_ROOT/%{_bindir}/
install yum/apt-dater-host.conf $RPM_BUILD_ROOT/%{_sysconfdir}/
install man/apt-dater-host.1 $RPM_BUILD_ROOT/%{_mandir}/man1/


%files
%doc README
%{_bindir}/apt-dater-host
%config %{_sysconfdir}/apt-dater-host.conf
%{_mandir}/man1/apt-dater-host.1*


%changelog
* Sat Dec  3 2016 Mike Gerber <mike@sprachgewalt.de>
- First package

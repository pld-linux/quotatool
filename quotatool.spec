Summary:	Utility for setting filesystem quotas from the command line.
Name:		quotatool
Version:	1.4.0
Release:	0.1
License:	GPL
Source0:	http://quotatool.ekenberg.se/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Group:		Applications/Console
URL:		http://quotatool.ekenberg.se/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quotatool is a utility to set filesystem quotas from the commandline.
Most quota-utilities are interactive, requiring manual intervention
from the user. Quotatool on the other hand is not, making it suitable
for use in scripts and other non-interactive situations.

%prep
%setup -q
%patch0 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man8}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

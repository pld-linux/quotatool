Summary:	Utility for setting filesystem quotas from the command line
Summary(pl.UTF-8):	Narzędzie do ustawiania ograniczeń w systemach plików z linii poleceń
Name:		quotatool
Version:	1.4.9
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://quotatool.ekenberg.se/%{name}-%{version}.tar.gz
# Source0-md5:	ad5fbae6d902fec8a9d166591973bcfa
Patch0:		%{name}-DESTDIR.patch
URL:		http://quotatool.ekenberg.se/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quotatool is a utility to set filesystem quotas from the commandline.
Most quota-utilities are interactive, requiring manual intervention
from the user. Quotatool on the other hand is not, making it suitable
for use in scripts and other non-interactive situations.

%description -l pl.UTF-8
Quotatool to narzędzie do ustawiania ograniczeń (quot) w systemie
plików z linii poleceń. Większość narzędzi do tego jest interaktywna,
wymagająca ręcznej interwencji użytkownika. Quotatool takie nie jest,
co czyni je użytecznym w skryptach i innych nieinteraktywnych
sytuacjach.

%prep
%setup -q
%patch0 -p0

%build
rm -rf autom4te.cache
cp -f /usr/share/automake/config.* ./tools
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

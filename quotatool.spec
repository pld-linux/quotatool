Summary:	Utility for setting filesystem quotas from the command line
Summary(pl):	Narzêdzie do ustawiania ograniczeñ w systemach plików z linii poleceñ
Name:		quotatool
Version:	1.4.3
Release:	0.1
License:	GPL
Group:		Applications/Console
Source0:	http://quotatool.ekenberg.se/%{name}-%{version}.tar.gz
# Source0-md5:	274c64e4fbf2f2029a4195836e8ac8b9
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

%description -l pl
Quotatool to narzêdzie do ustawiania ograniczeñ (quot) w systemie
plików z linii poleceñ. Wiêkszo¶æ narzêdzi do tego jest interaktywna,
wymagaj±ca rêcznej interwencji u¿ytkownika. Quotatool takie nie jest,
co czyni je u¿ytecznym w skryptach i innych nieinteraktywnych
sytuacjach.

%prep
%setup -q
%patch0 -p0

%build
cp -f /usr/share/automake/config.* ./tools
%{__aclocal}
%{__autoconf}
%configure
%{__make}
mv -f man/quotatool.8~ man/quotatool.8

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

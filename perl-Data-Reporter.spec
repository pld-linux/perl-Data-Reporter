%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Reporter
%define		_noautoreq "perl(Sybase::DBlib)" "perl(Sybase::Sybperl)"
Summary:	Data::Reporter perl module
Summary(pl):	Modu³ perla Data::Reporter
Name:		perl-Data-Reporter
Version:	1.4
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Reporter module generates ascii reports from a Database or a
plain ascii file.

%description -l pl
Modu³ Data::Reporter generuje raporty na podstawie bazy danych lub
pliku tekstowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* bin/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_sitearch}/Data/Reporter.pm
%{perl_sitearch}/Data/Reporter
%dir %{perl_sitearch}/auto/Data/Reporter
%dir %{perl_sitearch}/auto/Data/Reporter/RepFormat
%{perl_sitearch}/auto/Data/Reporter/RepFormat/autosplit.ix
%{perl_sitearch}/auto/Data/Reporter/RepFormat/RepFormat.bs
%attr(755,root,root) %{perl_sitearch}/auto/Data/Reporter/RepFormat/RepFormat.so
%{perl_sitearch}/auto/libRepFormat
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

%define	pdir	Data
%define	pnam	Reporter
%define		_noautoreq "perl(Sybase::DBlib)" "perl(Sybase::Sybperl)"
%include	/usr/lib/rpm/macros.perl
Summary:	Data-Reporter perl module
Summary(pl):	Modu³ perla Data-Reporter
Name:		perl-Data-Reporter
Version:	1.3.1
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.005_03-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Reporter module generates ascii reports from a Database or a
plain ascii file.

%description -l pl
Modu³ Data-Reporter generuje raporty na podstawie bazy danych lub
pliku tekstowego.

%prep
%setup -q -n Data-Reporter-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* bin/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
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

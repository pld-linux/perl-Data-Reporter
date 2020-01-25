%define		pdir	Data
%define		pnam	Reporter
Summary:	Data::Reporter Perl module - report generator
Summary(pl.UTF-8):	Moduł Perla Data::Reporter - generator raportów
Name:		perl-Data-Reporter
Version:	1.4
Release:	19
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86911309c9be9a1d57c26c0d44ee9c4a
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Data-Reporter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	Sybase::DBlib Sybase::Sybperl

%description
Data::Reporter module generates ASCII reports from a database or a
plain ASCII file.

%description -l pl.UTF-8
Moduł Data::Reporter generuje raporty na podstawie bazy danych lub
pliku tekstowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* bin/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorarch}/Data/Reporter.pm
%{perl_vendorarch}/Data/Reporter
%dir %{perl_vendorarch}/auto/Data/Reporter
%dir %{perl_vendorarch}/auto/Data/Reporter/RepFormat
%{perl_vendorarch}/auto/Data/Reporter/RepFormat/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Data/Reporter/RepFormat/RepFormat.so
%{perl_vendorarch}/auto/libRepFormat
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

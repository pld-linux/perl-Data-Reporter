%include	/usr/lib/rpm/macros.perl
Summary:	Data-Reporter perl module
Summary(pl):	Modu³ perla Data-Reporter
Name:		perl-Data-Reporter
Version:	1.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Reporter-%{version}.tar.gz
Patch0:		perl-Data-Reporter-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
cp -a bin $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/Reporter
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	$RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}/{*ES,*rep} \
        README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz

%{perl_sitelib}/Data/Reporter.pm
%{perl_sitelib}/Data/Reporter
%{perl_sitearch}/auto/Data/Reporter

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}

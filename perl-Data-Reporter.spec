%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Data-Reporter perl module
Summary(pl):	Modu³ perla Data-Reporter
Name:		perl-Data-Reporter
Version:	1.2
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Reporter-%{version}.tar.gz
Patch:		perl-Data-Reporter-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Data-Reporter module generates ascii reports from a Database or a plain
ascii file.

%description -l pl
Modu³ Data-Reporter generuje raporty na podstawie bazy danych lub pliku
tekstowego.

%prep
%setup -q -n Data-Reporter-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}
cp -a bin	 $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/Reporter
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}/{*ES,*rep} \
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

/usr/src/examples/%{name}-%{version}

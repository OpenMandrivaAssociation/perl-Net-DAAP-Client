%define upstream_name    Net-DAAP-Client
%define upstream_version 0.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Cient for Apple iTunes DAAP service
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5::M4p)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(Net::DAAP::DMAP)
BuildArch:	noarch

%description
dapple is a DAAP library for Perl.  DAAP is the protocol built
on top of HTTP that Apple's iTunes 4 uses to share music.  Most
responses to DAAP requests contain a binary DMAP structure.
This is an incomplete release.  There are missing features.
See the TODO file for future plans.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DAAP/Client.pm
%{perl_vendorlib}/Net/DAAP/Client/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.0
+ Revision: 404067
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.42-4mdv2009.0
+ Revision: 258003
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.42-3mdv2009.0
+ Revision: 246055
- rebuild

* Sun Mar 23 2008 Stefan van der Eijk <stefan@mandriva.org> 0.42-1mdv2008.1
+ Revision: 189590
- BuildRequires: perl-libwww-perl
- add missing BuildRequires: perl-Net-DAAP-DMAP
- fix License & Group
- import perl-Net-DAAP-Client



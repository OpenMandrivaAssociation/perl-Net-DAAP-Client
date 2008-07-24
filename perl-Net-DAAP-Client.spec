%define realname Net-DAAP-Client

Summary: Cient for Apple iTunes DAAP service
Name: perl-Net-DAAP-Client
Version: 0.42
Release: %mkrel 3
License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-DAAP-Client/
Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Net-DAAP-Client-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl-Digest-MD5-M4p
BuildRequires: perl-libwww-perl
BuildRequires: perl-Net-DAAP-DMAP

%description
dapple is a DAAP library for Perl.  DAAP is the protocol built
on top of HTTP that Apple's iTunes 4 uses to share music.  Most
responses to DAAP requests contain a binary DMAP structure.
This is an incomplete release.  There are missing features.
See the TODO file for future plans.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DAAP/Client.pm
%{perl_vendorlib}/Net/DAAP/Client/*

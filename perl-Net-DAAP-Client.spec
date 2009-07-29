%define upstream_name    Net-DAAP-Client
%define upstream_version 0.42

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Cient for Apple iTunes DAAP service
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl-Digest-MD5-M4p
BuildRequires: perl-libwww-perl
BuildRequires: perl-Net-DAAP-DMAP
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
dapple is a DAAP library for Perl.  DAAP is the protocol built
on top of HTTP that Apple's iTunes 4 uses to share music.  Most
responses to DAAP requests contain a binary DMAP structure.
This is an incomplete release.  There are missing features.
See the TODO file for future plans.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

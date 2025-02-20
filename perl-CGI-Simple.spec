#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : perl-CGI-Simple
Version  : 1.281
Release  : 43
URL      : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/CGI-Simple-1.281.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/CGI-Simple-1.281.tar.gz
Summary  : 'A Simple totally OO CGI interface that is CGI.pm compliant'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-CGI-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::NoWarnings)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
CGI-Simple version 1.114
INSTALLATION
To install this module, run the following commands:

%package dev
Summary: dev components for the perl-CGI-Simple package.
Group: Development
Provides: perl-CGI-Simple-devel = %{version}-%{release}
Requires: perl-CGI-Simple = %{version}-%{release}

%description dev
dev components for the perl-CGI-Simple package.


%package perl
Summary: perl components for the perl-CGI-Simple package.
Group: Default
Requires: perl-CGI-Simple = %{version}-%{release}

%description perl
perl components for the perl-CGI-Simple package.


%prep
%setup -q -n CGI-Simple-1.281
cd %{_builddir}/CGI-Simple-1.281
pushd ..
cp -a CGI-Simple-1.281 buildavx2
popd
pushd ..
cp -a CGI-Simple-1.281 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CGI::Simple.3
/usr/share/man/man3/CGI::Simple::Cookie.3
/usr/share/man/man3/CGI::Simple::Standard.3
/usr/share/man/man3/CGI::Simple::Util.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

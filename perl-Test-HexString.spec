#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	HexString
Summary:	Test::HexString - test binary strings with hex dump diagnostics
Name:		perl-Test-HexString
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7da5d58855789fd4326bfd172a990a8c
URL:		http://search.cpan.org/dist/Test-HexString/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This testing module provides a single function, is_hexstr(), which
asserts that the given string matches what was expected. When the
strings match (i.e. compare equal using the eq operator), the
behaviour is identical to the usual is() function provided by
Test::More.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Test/HexString.pm
%{_mandir}/man3/Test::HexString.3pm*

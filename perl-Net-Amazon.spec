#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	Amazon
Summary:	Net::Amazon - framework for accessing amazon.com via SOAP and XML/HTTP
Summary(pl.UTF-8):	Net::Amazon - szkielet do dostępu do amazon.com poprzez SOAP i XML/HTTP
Name:		perl-Net-Amazon
Version:	0.61
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	33192ac55aa6c4b3ccd3db097c5b2e6d
URL:		http://search.cpan.org/dist/Net-Amazon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Log-Log4perl >= 0.30
BuildRequires:	perl-URI
BuildRequires:	perl-XML-Simple >= 2.08
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Amazon provides an object-oriented interface to amazon.com's SOAP
and XML/HTTP interfaces. This way it's possible to create applications
using Amazon's vast amount of data via a functional interface, without
having to worry about the underlying communication mechanism.

%description -l pl.UTF-8
Net::Amazon oferuje zorientowany obiektowo dostęp do interfejsów SOAP
i XML/HTTP serwisu amazon.com. W ten sposób można tworzyć aplikacje
korzystające z przepastnych zasobów Amazonu poprzez funkcjonalny
interfejs, bez martwienia się o mechanizm komunikacyjny.

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
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/Amazon.pm
%{_mandir}/man3/*

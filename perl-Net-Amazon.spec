
# Conditional build:
%bcond_with	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Amazon
Summary:	Framework for accessing amazon.com via SOAP and XML/HTTP
Summary(pl):	Szkielet do dostêpu do amazon.com poprzez SOAP i XML/HTTP
Name:		perl-Net-Amazon
Version:	0.16
Release:	1
License:	Same as Perl itself
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7b86a8726ff99c5203d3bdd8d879765
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-libwww
BuildRequires:	perl-Log-Log4perl >= 0.30
BuildRequires:	perl(Test::More)
BuildRequires:	perl-URI
BuildRequires:	perl-XML-Simple >= 2.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Amazon provides an object-oriented interface to amazon.com's SOAP
and XML/HTTP interfaces. This way it's possible to create applications
using Amazon's vast amount of data via a functional interface, without
having to worry about the underlying communication mechanism.

%description -l pl
Net::Amazon oferuje zorientowany obiektowo dostêp do interfejsów SOAP
i XML/HTTP serwisu amazon.com. W ten sposób mo¿na tworzyæ aplikacje
korzystaj±ce z przepastnych zasobów Amazonu poprzez funkcjonalny
interfejs, bez martwienia siê o mechanizm komunikacyjny.

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

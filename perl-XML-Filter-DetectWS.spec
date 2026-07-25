%define modname	XML-Filter-DetectWS
%define modver	0.01

Summary:	XML::Filter::DetectWS - a PerlSAX filter that detects ignorable whitespace
Name:		perl-%{modname}
Version:	%{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	https://metacpan.org/dist/XML-Filter-DetectWS
Source0:	https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-Filter-DetectWS-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Filter-SAXT
Provides:	perl-libxml-enno = %{version}-%{release}

%description
This a PerlSAX filter that detects which character data contains
ignorable whitespace and optionally filters it.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/Filter/DetectWS.pm
%{_mandir}/man3/*


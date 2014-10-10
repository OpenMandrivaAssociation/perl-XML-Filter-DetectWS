%define modname	XML-Filter-DetectWS
%define modver	0.01

Summary:	XML::Filter::DetectWS - a PerlSAX filter that detects ignorable whitespace
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
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


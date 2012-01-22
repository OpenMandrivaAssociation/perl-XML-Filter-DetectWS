%define upstream_name    XML-Filter-DetectWS
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 4

Summary:	XML::Filter::DetectWS - a PerlSAX filter that detects ignorable whitespace
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-XML-Filter-SAXT
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno

%description
This a PerlSAX filter that detects which character data contains
ignorable whitespace and optionally filters it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/Filter/DetectWS.pm
%{_mandir}/*/*

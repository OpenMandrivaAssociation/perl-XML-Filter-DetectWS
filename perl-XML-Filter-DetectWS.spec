%define real_name XML-Filter-DetectWS

Summary:	XML::Filter::DetectWS - a PerlSAX filter that detects ignorable whitespace
Name:		perl-%{real_name}
Version:	0.01
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Filter-SAXT
BuildArch:	noarch
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno

%description
This a PerlSAX filter that detects which character data contains
ignorable whitespace and optionally filters it.

%prep
%setup -q -n %{real_name}-%{version} 

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



%define upstream_name    XML-Filter-DetectWS
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	XML::Filter::DetectWS - a PerlSAX filter that detects ignorable whitespace
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-XML-Filter-SAXT
BuildArch:	noarch
Provides:	perl-libxml-enno = %{version}-%{release}

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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/Filter/DetectWS.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4mdv2012.0
+ Revision: 765841
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3
+ Revision: 764337
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2
+ Revision: 667418
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 401862
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.01-5mdv2009.0
+ Revision: 224621
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-4mdv2008.1
+ Revision: 180654
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.01-3mdv2007.0
+ Revision: 85621
- Import perl-XML-Filter-DetectWS

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.01-3
- rebuild

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-2mdk
- fix deps

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdk
- initial Mandriva package


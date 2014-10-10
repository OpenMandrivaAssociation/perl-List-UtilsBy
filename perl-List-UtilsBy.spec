%define upstream_name    List-UtilsBy
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.09
Release:	2

Summary:	Higher-order list utility functions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/List/List-UtilsBy-0.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module provides a number of list utility functions, all of which take
an initial code block to control their behaviour. They are variations on
similar core perl or 'List::Util' functions of similar names, but which use
the block to control their behaviour. For example, the core Perl function
'sort' takes a list of values and returns them, sorted into order by their
string value. The 'sort_by' function sorts them according to the string
value returned by the extra function, when given each value.

 my @names_sorted = sort @names;

 my @people_sorted = sort_by { $_->name } @people;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 659937
- update to new version 0.07

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2
+ Revision: 656935
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 602044
- import perl-List-UtilsBy



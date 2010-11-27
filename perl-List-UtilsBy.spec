%define upstream_name    List-UtilsBy
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Higher-order list utility functions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/List/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*



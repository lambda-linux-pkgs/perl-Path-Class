Name:		perl-Path-Class
Version:	0.33
Release:	1%{?dist}
Summary:	Cross-platform path specification manipulation
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Path-Class/
Source0:	http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec) >= 3.26
BuildRequires:	perl(File::stat)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Module::Build) > 0.36
BuildRequires:	perl(parent)
BuildRequires:	perl(Perl::OSType)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Perl::Critic)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Path::Class is a module for manipulation of file and directory specifications
(strings describing their locations, like '/home/ken/foo.txt' or
'C:\Windows\Foo.txt') in a cross-platform manner. It supports pretty much every
platform Perl runs on, including Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2,
and NetWare.

%prep
%setup -q -n Path-Class-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}

%check
AUTHOR_TESTING=1 ./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Path/
%{_mandir}/man3/Path::Class.3pm*
%{_mandir}/man3/Path::Class::Dir.3pm*
%{_mandir}/man3/Path::Class::Entity.3pm*
%{_mandir}/man3/Path::Class::File.3pm*

%changelog
* Thu Dec 12 2013 Paul Howarth <paul@city-fan.org> - 0.33-1
- Update to 0.33:
  - New copy_to() and move_to() methods
  - As advised in the utime() docs, pass undef as the time for touch()
  - Do a better job cleaning up temp files in the tests
  - Optimization: use parent.pm instead of base.pm
  - Changed the docs to show that file() and dir() are exported by default
  - Fixed spelling error in POD
- Update buildreqs as needed
- Drop patch for building with old Module::Build versions

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.32-2
- Perl 5.18 rebuild

* Tue Mar 19 2013 Paul Howarth <paul@city-fan.org> - 0.32-1
- Update to 0.32:
  - Updated dependency on File::Spec to 3.26 (CPAN RT#83143)
  - Fixed bug with leading empty string in dir() - became unintentional
    UNC path on Cygwin
  - Fixed "Unterminated C<...> sequence" in Pod

* Thu Mar  7 2013 Paul Howarth <paul@city-fan.org> - 0.31-2
- Bump perl(File::Spec) version requirement to 3.26 (CPAN RT#83143)
- Drop EL-5 support since it doesn't have File::Spec ≥ 3.26

* Tue Feb  5 2013 Paul Howarth <paul@city-fan.org> - 0.31-1
- Update to 0.31:
  - Optimization: stringify variables passed to canonpath
  - Optimization: Use internal guts when constructing Dirs from Dirs, instead
    of concatenating and splitting them again with File::Spec
  - Fix grammar error in docs
  - Implement a 'split' parameter for the slurp() method
  - In docs, replace unicode MINUS SIGN with ascii HYPHEN-MINUS
- BR: perl(Scalar::Util)

* Tue Dec 18 2012 Paul Howarth <paul@city-fan.org> - 0.29-1
- Update to 0.29:
  - Add components() method, which returns directory names (and filename, if
    this is a File object) as a list
  - Fix a test failure on non-Unix platforms; the 07-recurseprune.t test was
    written in a Unix-specific way

* Mon Dec 17 2012 Paul Howarth <paul@city-fan.org> - 0.28-1
- Update to 0.28:
  - Fix test failures when run as root - they were relying on permissions
    failures, but permissions never fail as root
  - Add links in docs to the other modules we rely on and talk about in the
    docs, which makes for easier viewing through search.cpan.org / MetaCPAN
  - Fixed some misleading variable names in docs (CPAN RT#81795)

* Mon Dec 10 2012 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27:
  - Added pruning support in dir->recurse(); if recurse callback returns
    $item->PRUNE, no children of this item will be analyzed
  - Documented 'basename' method for directories
  - Added traverse_if() function, which allows one to filter children before
    processing them
  - Added tempdir() function
- Package upstream LICENSE file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.26-2
- Perl 5.16 rebuild

* Fri Jun 15 2012 Paul Howarth <paul@city-fan.org> - 0.26-1
- Update to 0.26:
  - resolve() now includes the name of the non-existent file in the error
    message
  - New shortcut opena(), to open a file for appending
  - New spew() method that does the inverse of the slurp() method
  - Fixed a typo in a class name in the docs for Path::Class::Entity
- Drop %%defattr, redundant since rpm 4.4
- Drop conditional for EPEL-4 support (EL-4 now EOL-ed)

* Thu Feb 16 2012 Paul Howarth <paul@city-fan.org> - 0.25-1
- Update to 0.25:
  - resolve() now croak()s instead of die()s on non-existent file
  - Added a traverse() method for directories, based on the fmap_cont() method
    of Forest::Tree::Pure; it's an alternative to ->recurse, which allows for
    more control over how the recursion happens
  - Fixed a grammar error in the docs
  - Added a tempfile() method for Dir objects, which provides an interface to
    File::Temp (CPAN RT#60485)
  - Fixed a non-helpful fatal error message when calling resolve() on a path
    that doesn't exist; now dies with the proper "No such file or directory"
    message and exit status
- BR: perl(Test::Perl::Critic) and run author tests where possible
- Add patch to support building with Module::Build < 0.3601

* Thu Feb 16 2012 Paul Howarth <paul@city-fan.org> - 0.23-4
- Spec clean-up:
  - Add buildreqs for Perl core modules that might be dual-lived
  - Tidy %%description
  - Make %%files list more explicit
  - Don't use macros for commands
  - Use search.cpan.org source URL
  - BR: at least version 0.87 of File::Spec

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.23-2
- Perl mass rebuild

* Thu Apr 14 2011 Ian Burrell <ianburrell@gmail.com> - 0.23-1
- Update to 0.23

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-3
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-2
- Mass rebuild with perl-5.12.0

* Mon Feb 22 2010 Chris Weyl <cweyl@alumni.drew.edu> - 0.18-1
- Update to 0.18 (for latest DBIx::Class)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16-6
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-3
- Rebuild for new perl

* Thu Aug 16 2007 Ian Burrell <ianburrell@gmail.com> - 0.16-2
- Fix BuildRequires

* Mon Jan 29 2007 Ian Burrell <ianburrell@gmail.com> - 0.16-1
- Specfile autogenerated by cpanspec 1.69.1

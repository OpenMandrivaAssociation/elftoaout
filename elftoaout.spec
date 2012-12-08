%define	name	elftoaout
%define	version	2.3
%define	release	%mkrel 13

Summary:	A utility for converting ELF binaries to a.out binaries
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/elftoaout/%{name}-%{version}.tar.bz2
Patch0:		elftoaout-2.3-include.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The elftoaout utility converts a static ELF binary to a static a.out
binary.  If you're using an ELF system (i.e., Mandriva Linux) on a SPARC,
you'll need to run elftoaout on the kernel image so that the SPARC PROM
can netboot the image.

If you're installing Mandriva Linux on a SPARC, you'll need to install the
elftoaout package.

%prep
%setup -q
%patch0 -p1 -b .include

%build
%make CFLAGS="%{optflags}"

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -m0755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -m0644 %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3-13mdv2011.0
+ Revision: 664131
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-12mdv2011.0
+ Revision: 605100
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-11mdv2010.1
+ Revision: 522574
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.3-10mdv2010.0
+ Revision: 424385
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 2.3-9mdv2009.1
+ Revision: 364906
- bunzip the patch

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.3-9mdv2009.0
+ Revision: 220722
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.3-8mdv2008.1
+ Revision: 149695
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 26 2007 Adam Williamson <awilliamson@mandriva.org> 2.3-7mdv2008.0
+ Revision: 44354
- rebuild for 2008
- Import elftoaout



* Fri Jun 30 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.3-6mdv2007.0
- build on all archs
- let rpm take care of stripping the binary

* Sat Jan 14 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.3-5mdk
- fix 64 bit size (P0 from aurora)
- %%mkrel
- s/Mandrakelinux/Mandriva Linux/

* Sun Jan 23 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.3-4mdk
- rebuild
- fix summary-ended-with-dot

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.3-3mdk
- rebuild
- don't use the forbidden word;)

* Sun May 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.3-2mdk
- s/Red Hat/Mandrake/ in description

* Fri May 16 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.3-1mdk
- 2.3
- cleaned up
- s/Copyright/License/
- compile with $RPM_OPT_FLAGS

* Wed Jan 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.2-1mdk
- first mandrake version.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- rebuild for Raw Hide.

* Fri Jul 10 1998 Jeff Johnson <jbj@redhat.com>
- repackage ultrapenguin with build root.

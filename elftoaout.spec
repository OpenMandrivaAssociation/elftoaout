%define	name	elftoaout
%define	version	2.3
%define	release	%mkrel 7

Summary:	A utility for converting ELF binaries to a.out binaries
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/elftoaout/%{name}-%{version}.tar.bz2
Patch0:		elftoaout-2.3-include.patch.bz2

%description
The elftoaout utility converts a static ELF binary to a static a.out
binary.  If you're using an ELF system (i.e., Mandriva Linux) on a SPARC,
you'll need to run elftoaout on the kernel image so that the SPARC PROM
can netboot the image.

If you're installing Mandriva Linux on a SPARC, you'll need to install the
elftoaout package.

%prep
%setup -q
%patch -p1 -b .include

%build
%make CFLAGS="$RPM_OPT_FLAGS"

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

%define	name	elftoaout
%define	version	2.3
%define release	21

Summary:	A utility for converting ELF binaries to a.out binaries
Name:		elftoaout
Version:	2.3
Release:	21
License:	GPLv2
Group:		System/Kernel and hardware
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/elftoaout/%{name}-%{version}.tar.bz2
Patch0:		elftoaout-2.3-include.patch

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
install -m0755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m0644 %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


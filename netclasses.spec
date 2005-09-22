Summary:	Asynchronous communication library
Summary(pl):	Biblioteka do komunikacji asynchronicznej
Name:		netclasses
Version:	1.05
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/netclasses/%{name}-%{version}.tar.bz2
# Source0-md5:	4bb8b3c680b6c7f59f59db552c306bc8
URL:		http://www.gnustep.org/
BuildRequires:	gnustep-base-devel >= 1.7.3
Requires:	gnustep-base >= 1.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gsdir		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
netclasses is an asynchronous networking library that works on OS X
natively, and any of the multitude of platforms supported by GNUstep.
You've never seen an easier way to put together network applications!

%description -l pl
netclasses to biblioteka do komunikacji asynchronicznej dzia³aj±ca
natywnie na OS X oraz wielu platformach obs³ugiwanych przez GNUstepa.
Wg autorów nie ma ³atwiejszej metody ³±czenia aplikacji sieciowych.

%package devel
Summary:	Header files for netclasses library
Summary(pl):	Pliki nag³ówkowe biblioteki netclasses
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-base-devel >= 0.8.6-3

%description devel
Header files for netclasses library.

%description devel -l pl
Pliki nag³ówkowe biblioteki netclasses.

%prep
%setup -q

%build
. %{_gsdir}/System/Library/Makefiles/GNUstep.sh
%configure
%{__make} \
	messages=yes \
	GUI_LIB=gnu # hack
%{__make} -C Documentation \
	messages=yes \
	GUI_LIB=gnu # hack

%install
rm -rf $RPM_BUILD_ROOT
. %{_gsdir}/System/Library/Makefiles/GNUstep.sh
%{__make} install \
	GUI_LIB=gnu \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_gsdir}/System \
	GNUSTEP_LIBRARIES_ROOT=$RPM_BUILD_ROOT%{_gsdir}/System/Library/Bundles
%{__make} -C Documentation install \
	GUI_LIB=gnu \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_gsdir}/System \
	GNUSTEP_LIBRARIES_ROOT=$RPM_BUILD_ROOT%{_gsdir}/System/Library/Bundles

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%docdir %{_prefix}/System/Library/Documentation

%files devel
%defattr(644,root,root,755)
%docdir %{_prefix}/System/Library/Documentation
%{_gsdir}/System/Library/Documentation/Developer/netclasses
%dir %{_gsdir}/System/Library/Frameworks/netclasses.framework
%dir %{_gsdir}/System/Library/Frameworks/netclasses.framework/Versions
%dir %{_gsdir}/System/Library/Frameworks/netclasses.framework/Versions/1.05
%{_gsdir}/System/Library/Frameworks/netclasses.framework/Versions/1.05/Headers
%dir %{_gsdir}/System/Library/Frameworks/netclasses.framework/Versions/1.05/Resources
%{_gsdir}/System/Library/Frameworks/netclasses.framework/Versions/1.05/Resources/*.plist
%attr(755,root,root) %{_gsdir}/System/Library/Frameworks/netclasses.framework/Versions/1.05/%{gscpu}/%{gsos}/%{libcombo}/*.so.*

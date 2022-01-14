%global 		underscore_version $(echo %{version} | cut -d. -f1-3 --output-delimiter="_")
Summary:        An XML parser library
Name:           expat
Version:        2.4.1
Release:        2%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/GeneralLibraries
URL:            https://libexpat.github.io/
Source0:        https://github.com/libexpat/libexpat/releases/download/R_%{underscore_version}/%{name}-%{version}.tar.bz2
Patch0: CVE-2022-22827_653bcf.patch
Patch1: CVE-2022-22827_9f93e8.patch
Patch2: CVE-2022-22827_8e9f6e.patch
Requires:       %{name}-libs = %{version}-%{release}

%description
The Expat package contains a stream oriented C library for parsing XML.

%package devel
Summary:        Header and development files for expat
Requires:       %{name} = %{version}-%{release}

%description    devel
It contains the libraries and header files to create applications

%package libs
Summary:        Libraries for expat
Group:          System Environment/Libraries

%description libs
This package contains minimal set of shared expat libraries.

%prep
%autosetup -p1

%build
%configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}/%{_docdir}/%{name}
%{_fixperms} %{buildroot}/*

%check
%make_build check

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc AUTHORS Changes
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libexpat.so
%{_libdir}/cmake/expat-%{version}

%files libs
%license COPYING
%{_libdir}/libexpat.so.1*

%changelog
*   Fri Jan 14 2022 Mariner Autopatcher <cblmargh@microsoft.com> 2.4.1-2
-   Added patch file(s) CVE-2022-22827_653bcf.patch,
-   CVE-2022-22827_9f93e8.patch, CVE-2022-22827_8e9f6e.patch
* Fri Nov 19 2021 Max Brodeur-Urbas <maxbr@microsoft.com> - 2.4.1-1
- Update to 2.4.1
- License verified
- Removed reference to manfiles, generation causes circular dependency.

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 2.2.6-4
- Added %%license line automatically

*   Wed Apr 22 2020 Nicolas Ontiveros <niontive@microsoft.com> 2.2.6-3
-   Fix CVE-2018-20843.
-   Remove sha1 macro.
-   Update URL.
-   Update Source0.

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 2.2.6-2
-   Initial CBL-Mariner import from Photon (license: Apache2).

*   Thu Sep 20 2018 Sujay G <gsujay@vmware.com> 2.2.6-1
-   Bump expat version to 2.2.6

*   Tue Sep 26 2017 Anish Swaminathan <anishs@vmware.com> 2.2.4-1
-   Updating version, fixes CVE-2017-9233,  CVE-2016-9063, CVE-2016-0718

*   Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com> 2.2.0-2
-   Added -libs and -devel subpackages

*   Fri Oct 21 2016 Kumar Kaushik <kaushikk@vmware.com> 2.2.0-1
-   Updating Source/Fixing CVE-2015-1283.

*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.1.0-2
-   GA - Bump release of all rpms

*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 2.1.0-1
-   Initial build.	First version

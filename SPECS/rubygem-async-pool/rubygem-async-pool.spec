%global debug_package %{nil}
%global gem_name async-pool
Summary:        Provides support for connection pooling both singleplex and multiplex resources
Name:           rubygem-%{gem_name}
Version:        0.3.9
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/socketry/async-pool
Source0:        https://github.com/socketry/async-pool/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
Patch0:         remove-pem.patch
BuildRequires:  ruby
Requires:       rubygem-async

%description
Provides support for connection pooling both singleplex and multiplex resources.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Mon Jan 04 2021 Henry Li <lihl@microsoft.com> - 0.3.3-1
- License verified
- Original version for CBL-Mariner

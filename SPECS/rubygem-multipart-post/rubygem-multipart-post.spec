%global debug_package %{nil}
%global gem_name multipart-post
Summary:        Adds multipart POST capability to net/http
Name:           rubygem-%{gem_name}
Version:        2.1.1
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/socketry/multipart-post
Source0:        https://github.com/socketry/multipart-post/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby

%description
Adds a streamy multipart form post capability to Net::HTTP.
Also supports other methods besides POST.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem
#add LICENSE file to buildroot from Source0
cp LICENSE %{buildroot}%{gem_instdir}/

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gemdir}

%changelog
* Wed Jan 06 2021 Henry Li <lihl@microsoft.com> - 2.1.1-1
- License verified
- Original version for CBL-Mariner

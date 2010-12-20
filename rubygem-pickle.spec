%define oname pickle

Name:       rubygem-%{oname}
Version:    0.2.12
Release:    %mkrel 1
Summary:    Easy model creation and reference in your cucumber features
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/ianwhite/pickle/tree
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(cucumber) >= 0.8
Requires:   rubygem(yard)
Requires:   rubygem(rspec)
Requires:   rubygem(rake)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Easy model creation and reference in your cucumber features

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/rails_generators/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/init.rb
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/License.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile*
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Todo.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

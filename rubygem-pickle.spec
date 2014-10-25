%define rbname pickle

Summary:	Easy model creation and reference in your cucumber features
Name:		rubygem-%{rbname}
Version:	0.4.11
Release:	1
License:	MIT
Group:		Development/Ruby
Url:		http://rubygems.org/downloads/%{rbname}
Source0:	http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
Easy model creation and reference in your cucumber features.

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}/
%{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 0.4.11

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

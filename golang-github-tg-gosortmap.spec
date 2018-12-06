# Run tests in check section
%bcond_without check

%global goipath         github.com/tg/gosortmap
%global commit          2901ada5a47d9fdeb1828c1d6d7e9585656bf0ba
%global common_description %{expand:
Sort maps in Go by keys or values. Works with most built-in types;
own comparator can be provided to support custom types and ordering.}

Version:        0

%gometa

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Sort maps in Go 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Tue Aug 14 2018 Gabe <redhatrises@gmail.com> - 0-0.1.20180814git2901ada
- First package for Fedora

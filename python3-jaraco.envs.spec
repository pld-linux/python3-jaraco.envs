#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests

Summary:	Classes for orchestrating Python (virtual) environments
Summary(pl.UTF-8):	Klasy do orkiestracji (wirtualnych) środowisk Pythona
Name:		python3-jaraco.envs
Version:	2.6.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco-envs/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco-envs/jaraco.envs-%{version}.tar.gz
# Source0-md5:	d5e22c491b6f73f1f1dd3d0261b0aa5c
URL:		https://pypi.org/project/jaraco.envs/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:56
BuildRequires:	python3-setuptools_scm >= 3.4.1
%if %{with tests}
BuildRequires:	python3-path
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-virtualenv
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-jaraco.packaging >= 9.3
BuildRequires:	python3-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-3 >= 3.5
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes for orchestrating Python (virtual) environments.

%description -l pl.UTF-8
Klasy do orkiestracji (wirtualnych) środowisk Pythona.

%package apidocs
Summary:	API documentation for Python jaraco.envs module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona jaraco.envs
Group:		Documentation

%description apidocs
API documentation for Python jaraco.envs module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona jaraco.envs.

%prep
%setup -q -n jaraco.envs-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst 
%{py3_sitescriptdir}/jaraco/envs.py
%{py3_sitescriptdir}/jaraco/__pycache__/envs.cpython-*.pyc
%{py3_sitescriptdir}/jaraco_envs-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif

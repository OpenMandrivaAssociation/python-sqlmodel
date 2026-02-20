%define module sqlmodel
%bcond tests 1

Name:		python-sqlmodel
Version:	0.0.35
Release:	1
Summary:	SQL databases in Python, designed for simplicity, compatibility, and robustness
URL:		https://pypi.org/project/sqlmodel/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sqlmodel/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sqlalchemy)
BuildRequires:	python%{pyver}dist(pydantic)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(black)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(dirty-equals)
BuildRequires:	python%{pyver}dist(fastapi)
BuildRequires:	python%{pyver}dist(httpx)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(typing-extensions)
%endif

%description
SQLModel is a library for interacting with SQL databases from Python code,
with Python objects.

It is designed to be intuitive, easy to use, highly compatible, and robust.

SQLModel is based on Python type annotations, and powered by
Pydantic and SQLAlchemy.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
# remove sqlmodel tests that require old python versions which cause-
# test failures
rm -rf docs_src/tutorial/fastapi/app_testing/tutorial001_py{39,310}/test*.py \
	tests/test_tutorial/test_fastapi/test_app_testing/test*.py \
	tests/test_select_gen.py \
	tests/test_tutorial/test_create_db_and_table/test_tutorial001*.py

export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.md

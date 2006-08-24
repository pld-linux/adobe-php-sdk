Summary:	Helping PHP developers build RIAs with Adobe technology
Summary(pl):	Pomoc dla programistów PHP w tworzeniu RIA z u¿yciem technologii Adobe
Name:		adobe-php-sdk
Version:	0
Release:	0.1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://blogs.adobe.com/mikepotter/adobe_php_sdk.zip
# Source0-md5:	bff4b02924791cc965d0a4fa06cf2bce
URL:		http://code.google.com/p/adobe-php-sdk/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Using the Adobe Spry Ajax framework and Adobe Flex, this SDK is
intended to help PHP developers build cool rich Internet applications
with Adobe technologies.

%description -l pl
Przy u¿yciu szkieletu Adobe Spry Ajax i Adobe Flex to SDK ma pomóc
programistom PHP w tworzeniu dobrych, bogatych aplikacji Internetowych
z u¿yciem technologii Adobe.

%prep
%setup -q -n adobe_php_sdk

# remove SVN control files
find -name .svn -print | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT

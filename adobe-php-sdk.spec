Summary:	Helping PHP developers build RIAs with Adobe technology
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
intended to help PHP developers build cool rich internet applications
with Adobe technologies.

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

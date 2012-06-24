%define		mver	%(echo %{version} |cut -f 1-2 -d ".")
Summary:	net top
Summary(pl):	Sieciowy top
Name:		nethogs
Version:	0.5.1
Release:	1
License:	GPL
Group:		Networking
Source0:	http://nethogs.bzzt.net/source/%{name}-%{version}.tar.gz
# Source0-md5:	542d489f3e1aaea2b2583511b855da00
URL:		http://nethogs.bzzt.net/
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetHogs is a small 'net top' tool. Instead of breaking the traffic
down per protocol or per subnet, like most such tools do, it groups
bandwidth by process - and does not rely on a special kernel module to
be loaded. So if there's suddenly a lot of network traffic, you can
fire up NetHogs and immediately see which PID is causing this, and if
it's some kind of spinning process, kill it.

%description -l pl
NetHogs to ma�e narz�dzie sieciowe w stylu programu top. Zamiast
rozbijania ruchu na protoko�y lub podsieci, jak robi wi�kszo��
narz�dzi, grupuje pasmo wed�ug proces�w - i nie polega przy tym na
specjalnym module j�dra. Je�li nagle jest du�y ruch w sieci, mo�na
uruchomi� NetHogs i od razu zobaczy�, kt�ry PID to powoduje i
ewentualnie go zabi�.

%prep
%setup -q -n %{name}-%{mver}

%build
%{__make} \
	GCC="%{__cxx}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install %{name}   $RPM_BUILD_ROOT%{_bindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

#%%define		mver	%(echo %{version} |cut -f 1-2 -d ".")
Summary:	net top
Summary(pl.UTF-8):	Sieciowy top
Name:		nethogs
Version:	0.7.0
Release:	1
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/nethogs/%{name}-%{version}.tar.gz
# Source0-md5:	e5f04071571e469e14c89f637cfa34a2
URL:		http://nethogs.sourceforge.net/
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

%description -l pl.UTF-8
NetHogs to małe narzędzie sieciowe w stylu programu top. Zamiast
rozbijania ruchu na protokoły lub podsieci, jak robi większość
narzędzi, grupuje pasmo według procesów - i nie polega przy tym na
specjalnym module jądra. Jeśli nagle jest duży ruch w sieci, można
uruchomić NetHogs i od razu zobaczyć, który PID to powoduje i
ewentualnie go zabić.

%prep
%setup -q -n %{name}

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
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

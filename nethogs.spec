Summary:	net top
Summary(pl.UTF-8):	Sieciowy top
Name:		nethogs
Version:	0.8.1
Release:	1
License:	GPL
Group:		Networking
Source0:	http://github.com/raboof/nethogs/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	cc0aed87c4cc67fc2ffc5f60aa67bf3d
URL:		http://raboof.github.io/nethogs/
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
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -I/usr/include/ncurses" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags} -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

cp -p %{name}   $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog DESIGN README.md
%attr(755,root,root) %{_bindir}/nethogs
%{_mandir}/man8/nethogs.8*

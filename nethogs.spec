Summary:	net top
Summary(pl):	Sieciowy top
Name:		nethogs
Version:	0.3
Release:	1
License:	GPL
Group:		Networking
Source0:	http://nethogs.bzzt.net/source/%{name}-%{version}.tar.gz
# Source0-md5:	439b67fc8c875a3142687758a2c61deb
Patch0:		%{name}-cxx.patch
Patch1:		%{name}-comp.patch
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
NetHogs to ma³e narzêdzie sieciowe w stylu programu top. Zamiast
rozbijania ruchu na protoko³y lub podsieci, jak robi wiêkszo¶æ
narzêdzi, grupuje pasmo wed³ug procesów - i nie polega przy tym na
specjalnym module j±dra. Je¶li nagle jest du¿y ruch w sieci, mo¿na
uruchomiæ NetHogs i od razu zobaczyæ, który PID to powoduje i
ewentualnie go zabiæ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	compiler="%{__cxx}" \
	flags="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

Summary:	Panel applet to manage the aRts sound server
Summary(pl.UTF-8):   Aplet panelu do kontroli serwera dźwięku aRts
Name:		kickarts
Version:	0.4
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://ripi.net/software/kickarts/%{name}-%{version}.tar.gz
# Source0-md5:	2cee1c1f1d0117cc42cc6dadb90c900a
URL:		http://ripi.net/software/kickarts/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kickarts is a simple panel applet to manage the aRts sound server. It
has basically the same features as the command-line utility artsshell
and is useful for quickly suspending or terminating the sound server
before launching an incompatible audio application.

%description -l pl.UTF-8
Kickarts to prosty aplet panelu do kontroli serwera dźwięku aRts. Ma
zasadniczo te same możliwości co narzędzie działające z linii poleceń
- artsshell - i jest użyteczny do szybkiego zatrzymania lub wyłączenia
serwera dźwięku przed załadowaniem niekompatybilnej aplikacji audio.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
cp -f /usr/share/automake/config.sub admin
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kickarts*.so
%{_libdir}/kde3/kickarts*.la
%{_datadir}/apps/kickarts
%{_datadir}/apps/kicker/applets/kickarts.desktop

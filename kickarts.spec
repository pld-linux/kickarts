Summary:	Panel applet to manage the aRts sound server
Summary(pl):	Panel applet do kontroli serwera d�wi�ku aRts
Name:		kickarts
Version:	0.4
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ripi.net/software/kickarts/%{name}-%{version}.tar.gz
URL:		http://ripi.net/software/kickarts/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	xmms-devel
Requires:	xmms
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Kickarts is a simple panel applet to manage the aRts sound server. It
has basically the same features as the command-line utility artsshell
and is useful for quickly suspending or terminating the sound server
before launching an incompatible audio application.

%description -l pl
Kickarts to prosty panel applet do kontroli serwera d�wi�ku aRts. Ma
zasadniczo te same mo�liwo�ci co narz�dzie linii polece� - artsshell i
jest u�yteczny do szybkiego zatrzymania lub wy��czenia serwera d�wi�ku
przed za�adowaniem niekompatybilnej aplikacji audio.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
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
%{_datadir}/apps/*
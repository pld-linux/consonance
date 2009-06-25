Summary:	a lightweight GTK+ music manager
Summary(pl.UTF-8):	lekki menadżer muzyczny oparty na GTK+
Name:		consonance
Version:	0.5.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	2a195dd2314f7b65cc57cc871a4c5a47
Source1:	%{name}.desktop
URL:		https://sites.google.com/site/consonancemanager/Home
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	flac-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libao-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	sqlite3-devel
BuildRequires:	taglib-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Consonance is a lightweight GTK+ music manager that aims to be fast,
bloat-free, and light on memory consumption. It is written completely
in C and GTK+. Some of the features are:
- Library management using sqlite3
- Multiple views
- OSD support
- Tag Editing
- mp3, ogg, flac, modplug, wav and Audio CD support
- Last.fm submission
- Playlist management (M3U)
- DBUS management interface

%description -l pl.UTF-8
Consonance jest lekkim menadżerem muzyki zbudowanym na GTK+, który
charakteryzuje się szybkością działania, brakiem zbędnych dodatków
oraz niskim zużyciem pamięci operacyjnej. Został w całości napisany w
C i GTK+. Oto niektóre z jego cech:
- Zarządzanie bibliotekami z wykorzystaniem sqlite3
- Różne widoki
- Wsparcie dla OSD
- Edycja tagów
- obsługa mp3, ogg, flac, modplug, wav i Audio CD
- obsługa Last.fm
- Zarządzanie listą odtwarzania (M3U)
- Interfejs zarządzania DBUS

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/consonance
%dir %{_datadir}/consonance
%dir %{_datadir}/consonance/data
%{_datadir}/consonance/data/*.png
%{_desktopdir}/consonance.desktop
%{_mandir}/man1/consonance.1*

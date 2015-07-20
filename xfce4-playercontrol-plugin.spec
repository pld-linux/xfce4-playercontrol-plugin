Summary:	XMMS, BMP or Audacious player control plugin
Summary(pl.UTF-8):	Wtyczka do kontroli odtwarzacza XMMS, BMP lub Audacious
Name:		xfce4-playercontrol-plugin
Version:	0.3.0
Release:	10
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://www.bilimfeneri.gen.tr/ilgar/%{name}-%{version}.tar.bz2
# Source0-md5:	307c896467e204706cf04942151f2fcc
Patch0:		%{name}-audclient.patch
Patch1:		%{name}-ui.patch
Patch2:		%{name}-panel48.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-GtkTooltips.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xmms-plugin
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libaudclient-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
BuildRequires:	xmms-devel
Requires:	xfce4-panel >= 4.4.0
Suggests:	%{name}-audacious
Suggests:	%{name}-xmms
Obsoletes:	xfce4-xmms-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin which provides you control on XMMS, BMP or Audacious media
player from Xfce panel.

%description -l pl.UTF-8
Wtyczka, która umożliwia kontrolę nad odtwarzaczem multimedialnym
XMMS, BMP lub Audacious z pozycji panelu Xfce.

%package audacious
Summary:	Audacious support for playercontrol plugin
Summary(pl.UTF-8):	Obsługa Audacious dla wtyczki playercontrol
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description audacious
Audacious support for playercontrol plugin.

%description audacious -l pl.UTF-8
Obsługa Audacious dla wtyczki playercontrol.

%package xmms
Summary:	XMMS support for playercontrol plugin
Summary(pl.UTF-8):	Obsługa XMMS dla wtyczki playercontrol
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description xmms
XMMS support for playercontrol plugin.

%description xmms -l pl.UTF-8
Obsługa XMMS dla wtyczki playercontrol.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-xmms \
	--enable-audacious \
	--disable-mpd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-playercontrol-plugin
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libplayercontrol_dummy.so
%{_datadir}/xfce4/panel-plugins/xfce4-playercontrol-plugin.desktop
%{_datadir}/xfce4/xfce4-playercontrol-plugin

%files audacious
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libplayercontrol_audacious.so

%files xmms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libplayercontrol_xmms.so

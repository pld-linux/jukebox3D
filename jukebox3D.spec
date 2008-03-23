Summary:	jukebox3D
Name:		jukebox3D
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		X11/Amusements
Source0:	http://j3d.linuxonfire.org/download/old/0.5.0/%{name}_EN.tar.gz
# Source0-md5:	1dbf791ae76b48f661b8a0ef826abd9e
Patch0:		%{name}-optflags.patch
URL:		http://j3d.linuxonfire.org/index.php?lang=1
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	curl-devel
BuildRequires:	glade2
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Player enhancer - Another way for displaying your playlist

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_datadir}/icons,%{_bindir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/jukebox3D
%{_datadir}/jukebox3d-0.5.0
%{_iconsdir}/j3dico.png
%{_desktopdir}/jukebox3D.desktop

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Office game for laptop owners
Name:		office-runner
Version:	1.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
Buildrequires:	itstool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Game for laptop users allowing you to inhibit suspend and record your timings.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-schemas-install

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*


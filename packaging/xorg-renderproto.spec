Name:           xorg-renderproto
Version:        0.11.1
Release:        0
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        http://xorg.freedesktop.org/releases/individual/proto/renderproto-%{version}.tar.gz
Source1001:     packaging/xorg-renderproto.manifest
Provides:       renderproto

BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}

%prep
%setup -q -n renderproto-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?_smp_mflags}

%install
%make_install


%files
%manifest xorg-renderproto.manifest
%{_libdir}/pkgconfig/renderproto.pc
%{_includedir}/X11/extensions/renderproto.h
%{_includedir}/X11/extensions/render.h
%doc %{_datadir}/doc/renderproto

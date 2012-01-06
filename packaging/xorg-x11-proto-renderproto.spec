
Name:       xorg-x11-proto-renderproto
Summary:    X.Org X11 Protocol renderproto
Version:    0.11.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/renderproto-%{version}.tar.gz
Provides:   renderproto

BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n renderproto-%{version}

%build

%reconfigure --disable-shared 

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/renderproto.pc
%{_includedir}/X11/extensions/renderproto.h
%{_includedir}/X11/extensions/render.h
%doc %{_datadir}/doc/renderproto



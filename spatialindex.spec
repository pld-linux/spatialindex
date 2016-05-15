Summary:	Spatial Index Library
Summary(pl.UTF-8):	Biblioteka Spatial Index
Name:		spatialindex
Version:	1.8.5
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://download.osgeo.org/libspatialindex/%{name}-src-%{version}.tar.bz2
# Source0-md5:	3303c47fd85aa17e64ef52ebec212762
#Patch0:		%{name}-mvtree.patch
URL:		https://libspatialindex.github.io/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a general framework for developing spatial
indices. Currently it defines generic interfaces, provides simple main
memory and disk based storage managers and a robust implementation of
an R*-tree, an MVR-tree and a TPR-tree.

%description -l pl.UTF-8
Ten pakiet zawiera ogólny szkielet do tworzenia indeksów
przestrzennych. Aktualnie definiuje ogólne interfejsy, udostępnia
proste zarządzanie główną pamięcią i przechowywaniem danych na dysku
oraz silną implementację drzew R*, MVR i TPR.

%package devel
Summary:	Header files for Spatial Index Library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Spatial Index
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Spatial Index Library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Spatial Index.

%package static
Summary:	Static version of Spatial Index Library
Summary(pl.UTF-8):	Statyczna wersja biblioteki Spatial Index
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Spatial Index Library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki Spatial Index.

%prep
%setup -q -n %{name}-src-%{version}
#%patch0 -p0

%build
%configure
%{__make} \
	LDFLAGS="-lm"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib%{name}*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib%{name}*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}*.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}*.so
%{_includedir}/spatialindex
%{_pkgconfigdir}/lib%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}*.a

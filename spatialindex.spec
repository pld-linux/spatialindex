Summary:	Spatial Index Library
Summary(pl.UTF-8):	Biblioteka Spatial Index
Name:		spatialindex
Version:	1.3.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://trac.gispython.org/projects/SpatialIndex/attachment/wiki/Releases/%{name}-%{version}.tar.gz?format=raw
# Source0-md5:	d7439c5b9cdefb80c73a5a39c7a8dc53
Patch0:		%{name}-mvtree.patch
URL:		http://research.att.com/~marioh/spatialindex/index.html
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

%description devel -l pl
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
%setup -q
#%patch0 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/spatialindex

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

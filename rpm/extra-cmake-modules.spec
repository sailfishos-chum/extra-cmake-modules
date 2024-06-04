Name:        opt-extra-cmake-modules
Version:     5.116.0
Release:     1
Summary:     The Extra CMake Modules package
License:     BSD
URL:         https://cgit.kde.org/extra-cmake-modules.git
Source0:     %{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: opt-kf5-rpm-macros
BuildArch: noarch

%description
The Extra CMake Modules package, or ECM, adds to the modules provided by CMake, including ones
used by find_package() to find common software, ones that can be used directly in CMakeLists.txt
files to perform common tasks and toolchain files that must be specified on the commandline by the user.


# define macros for SFOS 4.5 and lower, where the cmake package does not have them:
# these defines are taken from https://github.com/sailfishos/cmake/blob/master/rpm/macros.cmake.in
%if %{undefined _cmake_version}
#%%define __cmake_in_source_build 1
%define _vpath_srcdir .
%define _vpath_builddir %{_target_platform}
%define __cmake_builddir %{!?__cmake_in_source_build:%{_vpath_builddir}}%{?__cmake_in_source_build:.}
%define cmake_build %__cmake --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%define cmake_install DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}"
%endif


%prep
%autosetup -n %{name}-%{version}/upstream

%build
export QTDIR=%{_opt_qt5_prefix}

%{_opt_cmake_kf5}
%cmake_build

%install
%cmake_install

%files
%license COPYING-CMAKE-SCRIPTS
%{_opt_qt5_prefix}/share/ECM/modules/*
%{_opt_qt5_prefix}/share/ECM/test-modules/*
%{_opt_qt5_prefix}/share/ECM/kde-modules/*
%{_opt_qt5_prefix}/share/ECM/find-modules/*
%{_opt_qt5_prefix}/share/ECM/toolchain/*
%{_opt_qt5_prefix}/share/ECM/cmake/*

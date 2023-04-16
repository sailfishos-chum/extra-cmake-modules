Name:        opt-extra-cmake-modules
Version: 5.105.0
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

%prep
%autosetup -n %{name}-%{version}/upstream

%build
export QTDIR=%{_opt_qt5_prefix}

%{_opt_cmake_kf5}
%make_build

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING-CMAKE-SCRIPTS
%{_opt_qt5_prefix}/share/ECM/modules/*
%{_opt_qt5_prefix}/share/ECM/test-modules/*
%{_opt_qt5_prefix}/share/ECM/kde-modules/*
%{_opt_qt5_prefix}/share/ECM/find-modules/*
%{_opt_qt5_prefix}/share/ECM/toolchain/*
%{_opt_qt5_prefix}/share/ECM/cmake/*

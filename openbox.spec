%define		_snap 20030505

Summary:	Very small and fast window manger for the X Window
Summary(pl):	Ma³y i szybki zarz±dca okien dla X Window
Name:		openbox
Version:	2.3.1
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Window Managers
#Source0:	http://icculus.org/openbox/releases/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	c9a04288cc9c807b2d6d6d0c6f5c1707
Patch0:		%{name}-paths.patch
Patch1:		%{name}-gcc_3.3_fix.patch
Patch2:		%{name}-nls-codeset.patch
URL:		http://icculus.org/openbox/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	fontconfig-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	xft-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/%{name}

%description
Openbox is a window manager for the X11 windowing system. It currently
runs on a large list of platforms.

%description -l pl
Openbox jest zarz±dc± okien dla systemu X11. W chwili obecnej pracuje
na wielu platformach systemowych.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "Remember to copy from /etc/X11/openbox menu and epistrc "
echo "to your ~/.openbox dir. menu file should contain only"
echo "UTF-8 characters!"
echo

%files
%defattr(644,root,root,755)
%doc README* CHANGELOG TODO util/epist/ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%{_sysconfdir}/menu
%{_sysconfdir}/epistrc
%dir %{_datadir}/openbox
%{_datadir}/openbox/buttons
%{_datadir}/openbox/styles
%dir %{_datadir}/openbox/nls
%{_datadir}/openbox/nls/C
%lang(da) %{_datadir}/openbox/nls/da_DK
%lang(de) %{_datadir}/openbox/nls/de_DE
%lang(es_AR) %{_datadir}/openbox/nls/es_AR
%lang(es_ES) %{_datadir}/openbox/nls/es_ES
%lang(et) %{_datadir}/openbox/nls/et_ET
%lang(fr) %{_datadir}/openbox/nls/fr_FR
%lang(hu) %{_datadir}/openbox/nls/hu_HU
%lang(it) %{_datadir}/openbox/nls/it_IT
%lang(ja) %{_datadir}/openbox/nls/ja_JP
%lang(ko) %{_datadir}/openbox/nls/ko_KR
%lang(nl) %{_datadir}/openbox/nls/nl_NL
%lang(no) %{_datadir}/openbox/nls/no_NO
%lang(pl) %{_datadir}/openbox/nls/pl_PL
%lang(pt) %{_datadir}/openbox/nls/pt_BR
%lang(ro) %{_datadir}/openbox/nls/ro_RO
%lang(ru) %{_datadir}/openbox/nls/ru_RU
%lang(sk) %{_datadir}/openbox/nls/sk_SK
%lang(sl) %{_datadir}/openbox/nls/sl_SI
%lang(sv) %{_datadir}/openbox/nls/sv_SE
%lang(tr) %{_datadir}/openbox/nls/tr_TR
%lang(uk) %{_datadir}/openbox/nls/uk_UA
%lang(zh_CN) %{_datadir}/openbox/nls/zh_CN
%lang(zh_TW) %{_datadir}/openbox/nls/zh_TW
%{_mandir}/man1/*
%{_mandir}/man5/*

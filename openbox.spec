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
Patch0:		%{name}-paths.patch
URL:		http://icullus.org/openbox/
BuildRequires:	XFree86-devel
BuildRequires:	Xft-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	fontconfig-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
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
%dir %{_datadir}/nls
# TODO: add %{_datadir}/openbox/nls/* dirs with %lang(),
#	but maybe it's sufficient to include whole directories?
#	I'll check later...  --q
%{_datadir}/openbox/nls/C/%{name}.cat
%lang(da) %{_datadir}/openbox/nls/da_DK/%{name}.cat
%lang(de) %{_datadir}/openbox/nls/de_DE/%{name}.cat
%lang(es_AR) %{_datadir}/openbox/nls/es_AR/%{name}.cat
%lang(es_ES) %{_datadir}/openbox/nls/es_ES/%{name}.cat
%lang(et) %{_datadir}/openbox/nls/et_ET/%{name}.cat
%lang(fr) %{_datadir}/openbox/nls/fr_FR/%{name}.cat
%lang(hu) %{_datadir}/openbox/nls/hu_HU/%{name}.cat
%lang(it) %{_datadir}/openbox/nls/it_IT/%{name}.cat
%lang(ja) %{_datadir}/openbox/nls/ja_JP/%{name}.cat
%lang(ko) %{_datadir}/openbox/nls/ko_KR/%{name}.cat
%lang(nl) %{_datadir}/openbox/nls/nl_NL/%{name}.cat
%lang(no) %{_datadir}/openbox/nls/no_NO/%{name}.cat
%lang(pl) %{_datadir}/openbox/nls/pl_PL/%{name}.cat
%lang(pt) %{_datadir}/openbox/nls/pt_BR/%{name}.cat
%lang(ro) %{_datadir}/openbox/nls/ro_RO/%{name}.cat
%lang(ru) %{_datadir}/openbox/nls/ru_RU/%{name}.cat
%lang(sk) %{_datadir}/openbox/nls/sk_SK/%{name}.cat
%lang(sl) %{_datadir}/openbox/nls/sl_SI/%{name}.cat
%lang(sv) %{_datadir}/openbox/nls/sv_SE/%{name}.cat
%lang(tr) %{_datadir}/openbox/nls/tr_TR/%{name}.cat
%lang(uk) %{_datadir}/openbox/nls/uk_UA/%{name}.cat
%lang(zh_CN) %{_datadir}/openbox/nls/zh_CN/%{name}.cat
%lang(zh_TW) %{_datadir}/openbox/nls/zh_TW/%{name}.cat
%{_mandir}/man1/*
%{_mandir}/man5/*

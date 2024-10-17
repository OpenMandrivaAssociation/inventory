%define name	inventory
%define version 0.65
%define release  13

Name: 	 	%{name}
Summary: 	Simple GTK2 inventory program using MySQL
Version: 	%{version}
Release: 	%{release}

Source0:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		https://qballsinventory.sourceforge.net/
License:	GPL
Group:		Databases
BuildRequires:	pkgconfig pkgconfig(gtk+-2.0) mysql-devel

%description
Inventory is a gtk+-2 inventory program that uses a mysql database as backend.
Inventory can't do anything fancy, complicated or complex (like linked tables),
instead it tries to be flexible, multi-purpose and fast while remaining easy to
use.  Features include:

    * Mysql Backend.
    * User defined amount of columns in a table.
    * Every column can be either a string, integer or boolean.
    * Everything can be changed at any time. f.e. amount off column, column
      name, column type, category name, etc
    * Direct editing off data in the table, or in a pop-up window.
    * Export to html or comma seperated file.
    * Import from comma seperated file with preview.
    * User feedback, the program tries to give as much feedback as needed.
    * Responsive, changes are directly applyed in the gui, and synced with
      mysql.
    * When an error has occured, it gives the user the oppertunity to correct
      it.
    * Lots More

%prep
%setup -q -n %name

%build
%configure2_5x
%make
										
%install
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=Inventory
Comment=Simple Inventory Program
Categories=Database;Office;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name || touch %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/pixmaps/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.65-12mdv2011.0
+ Revision: 645805
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 0.65-11mdv2011.0
+ Revision: 627251
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.65-10mdv2011.0
+ Revision: 626530
- rebuilt against mysql-5.5.8 libs

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.65-8mdv2011.0
+ Revision: 619653
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.65-7mdv2010.0
+ Revision: 437962
- rebuild

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.65-6mdv2009.1
+ Revision: 311336
- rebuilt against mysql-5.1.30 libs

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.65-5mdv2009.0
+ Revision: 247233
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.65-3mdv2008.1
+ Revision: 132141
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import inventory


* Wed May 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.65-3mdk
- Rebuild

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 0.65-2mdk
- stale rebuild
- delib buildrequires
- configure 2.5

* Sun Mar 30 2003 Austin Acton <aacton@yorku.ca> 0.65-1mdk
- initial package

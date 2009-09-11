%define name	inventory
%define version 0.65
%define release  %mkrel 7

Name: 	 	%{name}
Summary: 	Simple GTK2 inventory program using MySQL
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://qballsinventory.sourceforge.net/
License:	GPL
Group:		Databases
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig gtk2-devel mysql-devel

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
rm -rf $RPM_BUILD_ROOT
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

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/pixmaps/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


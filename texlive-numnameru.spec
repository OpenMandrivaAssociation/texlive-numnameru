Name:		texlive-numnameru
Version:	44895
Release:	1
Summary:	Converts a number to the russian spelled out name
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numnameru
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numnameru.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numnameru.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package converts a numerical number to the russian spelled
out name of the number. For example, 1 - odin, 2 - dva, 12 -
dvenadtsat'.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/numnameru
%doc %{_texmfdistdir}/doc/latex/numnameru

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

Name:		texlive-heuristica
Version:	69649
Release:	1
Summary:	Fonts extending Utopia, with LaTeX support files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/heuristica
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts extend the utopia set with Cyrillic glyphs,
additional figure styles, ligatures and Small Caps in Regular
style only. Macro support, and maths fonts that match the
Utopia family, are provided by the Fourier and the Mathdesign
font packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/heuristica
%{_texmfdistdir}/fonts/map/dvips/heuristica
%{_texmfdistdir}/fonts/opentype/public/heuristica
%{_texmfdistdir}/fonts/tfm/public/heuristica
%{_texmfdistdir}/fonts/type1/public/heuristica
%{_texmfdistdir}/fonts/vf/public/heuristica
%{_texmfdistdir}/tex/latex/heuristica
%doc %{_texmfdistdir}/doc/fonts/heuristica

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

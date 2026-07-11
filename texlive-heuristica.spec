%global tl_name heuristica
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.093
Release:	%{tl_revision}.1
Summary:	Fonts extending Utopia, with LaTeX support files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/heuristica
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts extend the utopia set with Cyrillic glyphs, additional figure
styles, ligatures and Small Caps in Regular style only. Macro support,
and maths fonts that match the Utopia family, are provided by the
Fourier and the Mathdesign font packages.


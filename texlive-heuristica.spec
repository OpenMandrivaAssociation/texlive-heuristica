%global tl_name heuristica
%global tl_revision 79618
%global tl_version 1.093

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Fonts extending Utopia, with LaTeX support files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/heuristica
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The fonts extend the utopia set with Cyrillic glyphs, additional figure
styles, ligatures and Small Caps in Regular style only. Macro support,
and maths fonts that match the Utopia family, are provided by the
Fourier and the Mathdesign font packages.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from heuristica:
Map Heuristica.map
TL_DROPIN_EOF

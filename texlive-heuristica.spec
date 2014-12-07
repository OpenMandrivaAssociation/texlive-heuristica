# revision 34103
# category Package
# catalog-ctan /fonts/heuristica
# catalog-date 2014-05-18 18:31:37 +0200
# catalog-license ofl
# catalog-version 1.01
Name:		texlive-heuristica
Version:	1.01
Release:	3
Summary:	Fonts extending Utopia, with LaTeX support files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/heuristica
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/heuristica.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_3sseao.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_5b7xz5.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_75nckf.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_bv5hp7.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_ckaykl.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_cnmq22.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_dcwkkw.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_dhvb6d.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_dvh2xl.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_e7tlds.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_f5u5uq.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_faifug.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_flhghs.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_g4w54e.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_geqeyh.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_hbxdik.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_hdx6sb.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_hln2hy.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_ioi5s5.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_it5nv3.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_o6uy2f.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_oyyjpx.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_pwyhgk.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_qy67bk.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_rhmrtx.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_thxlbm.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_u7pc6m.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_vaioc2.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_vtjod4.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_zk7stm.enc
%{_texmfdistdir}/fonts/map/dvips/heuristica/Heuristica.map
%{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/TS1Heuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/TS1Heuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/heuristica.sty
%doc %{_texmfdistdir}/doc/fonts/heuristica/FontLog.txt
%doc %{_texmfdistdir}/doc/fonts/heuristica/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/heuristica/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/heuristica/README
%doc %{_texmfdistdir}/doc/fonts/heuristica/heuristica-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/heuristica/heuristica-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

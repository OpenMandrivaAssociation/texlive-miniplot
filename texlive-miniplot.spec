Name:		texlive-miniplot
Version:	20100314
Release:	1
Summary:	A package for easy figure arrangement
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/miniplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miniplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miniplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
MiniPlot is a package to help the LaTeX user typeset EPS
figures using an easy-to-use interface. Figures can be arranged
as one-figure-only or as a collection of figures in columns and
rows which can itself contain sub-figures in columns and rows.
Wrapped figures are also supported. This package provides
commands to display a framebox instead of the figure as the
graphics package does already but additionally it writes useful
information such as the label and scaling factor into these
boxes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/miniplot/miniplot.sty
%doc %{_texmfdistdir}/doc/latex/miniplot/disclaimer.txt
%doc %{_texmfdistdir}/doc/latex/miniplot/documentation.zip
%doc %{_texmfdistdir}/doc/latex/miniplot/miniplot.pdf
%doc %{_texmfdistdir}/doc/latex/miniplot/miniplot.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

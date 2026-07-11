%global tl_name miniplot
%global tl_revision 17483

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A package for easy figure arrangement
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/miniplot
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miniplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miniplot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MiniPlot is a package to help the LaTeX user typeset EPS figures using
an easy-to-use interface. Figures can be arranged as one-figure-only or
as a collection of figures in columns and rows which can itself contain
sub-figures in columns and rows. Wrapped figures are also supported.
This package provides commands to display a framebox instead of the
figure as the graphics package does already but additionally it writes
useful information such as the label and scaling factor into these
boxes.


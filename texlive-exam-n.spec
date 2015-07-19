# revision 33862
# category Package
# catalog-ctan /macros/latex/contrib/exam-n
# catalog-date 2014-05-05 22:16:32 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-exam-n
Version:	1.1
Release:	4
Summary:	Exam class, focused on collaborative authoring
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exam-n
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-n.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-n.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-n.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class design offers: Direct support for collaborative
development of an exam, using a model in which a departmental
'exams convener' or 'exam chair' coordinates multiple authors
writing individual questions (the class file and associated
process is in regular use within a physics and astronomy
department). All of the 'traditional' exam paper features such
as sectioning, per-part running marks, 'Question n continued'
catchwords, and so on. Readily configured local adaptation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exam-n/exam-n.cls
%doc %{_texmfdistdir}/doc/latex/exam-n/README
%doc %{_texmfdistdir}/doc/latex/exam-n/exam-n-example.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/exam-n.html
%doc %{_texmfdistdir}/doc/latex/exam-n/exam-n.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/lppl.txt
%doc %{_texmfdistdir}/doc/latex/exam-n/move-to-texmf/A1.clo
%doc %{_texmfdistdir}/doc/latex/exam-n/move-to-texmf/exam-n.cls
%doc %{_texmfdistdir}/doc/latex/exam-n/notes-for-authors.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/release-notes.html
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/Makefile
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/cosmo1.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/cosmo2.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/cosmo3.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/dynamical1.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/dynamical2.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/dynamical3.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/excos1.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/numerical1-solution.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/numerical1-solution.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/numerical1.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/numerical2.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/numerical3.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/sample_exam.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/sample_exam.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/sample_exam_solution.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/sample_exam_solution.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/sample_mcq.tex
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/spiral.eps
%doc %{_texmfdistdir}/doc/latex/exam-n/sample/spiral.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/sample_exam.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/sample_exam_solution.pdf
%doc %{_texmfdistdir}/doc/latex/exam-n/style.css
#- source
%doc %{_texmfdistdir}/source/latex/exam-n/exam-n.drv
%doc %{_texmfdistdir}/source/latex/exam-n/exam-n.dtx
%doc %{_texmfdistdir}/source/latex/exam-n/exam-n.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

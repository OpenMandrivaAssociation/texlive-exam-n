Name:		texlive-exam-n
Version:	1.1.4
Release:	2
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
%{_texmfdistdir}/tex/latex/exam-n
%doc %{_texmfdistdir}/doc/latex/exam-n
#- source
%doc %{_texmfdistdir}/source/latex/exam-n

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

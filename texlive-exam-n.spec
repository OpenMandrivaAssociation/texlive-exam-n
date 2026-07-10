%global tl_name exam-n
%global tl_revision 64674

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Exam class, focused on collaborative authoring
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exam-n
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-n.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-n.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-n.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class design offers: Direct support for collaborative development of
an exam, using a model in which a departmental 'exams convener' or 'exam
chair' coordinates multiple authors writing individual questions (the
class file and associated process is in regular use within a physics and
astronomy department). All of the 'traditional' exam paper features such
as sectioning, per-part running marks, 'Question n continued'
catchwords, and so on. Readily configured local adaptation.


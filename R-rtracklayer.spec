%bcond_with internet
%bcond_with bootstrap
%global packname  rtracklayer
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.18.2
Release:          1
Summary:          R interface to genome browsers and their annotation tracks
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/rtracklayer_1.18.2.tar.gz
Requires:         R-methods R-RCurl R-XML R-IRanges R-GenomicRanges
Requires:         R-Biostrings R-BSgenome R-zlibbioc
%if %{with bootstrap}
Requires:         R-microRNA R-genefilter R-org.Hs.eg.db
Requires:         R-BSgenome.Hsapiens.UCSC.hg19 R-hgu133plus2.db
%else
Requires:         R-humanStemCell R-microRNA R-genefilter R-limma
Requires:         R-org.Hs.eg.db R-BSgenome.Hsapiens.UCSC.hg19
Requires:         R-TxDb.Hsapiens.UCSC.hg19.knownGene R-hgu133plus2.db
Requires:         R-Rsamtools
Requires:         R-BiocGenerics
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-RCurl R-XML R-IRanges R-GenomicRanges R-Biostrings
BuildRequires:    R-BSgenome R-zlibbioc
BuildRequires:    R-BiocGenerics
%if %{with bootstrap}
BuildRequires:    R-microRNA R-genefilter R-org.Hs.eg.db
BuildRequires:    R-BSgenome.Hsapiens.UCSC.hg19 R-hgu133plus2.db
%else
BuildRequires:    R-humanStemCell R-microRNA R-genefilter R-limma
BuildRequires:    R-org.Hs.eg.db R-BSgenome.Hsapiens.UCSC.hg19
BuildRequires:    R-TxDb.Hsapiens.UCSC.hg19.knownGene R-hgu133plus2.db
BuildRequires:    R-Rsamtools
%endif

%description
Extensible framework for interacting with multiple genome browsers
(currently UCSC built-in) and manipulating annotation tracks in various
formats (currently GFF, BED, bedGraph, BED15, WIG, and BigWig built-in).
The user may export/import tracks to/from the supported browsers, as well
as query and modify the browser state, such as the current viewport.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
    %if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
    %endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/notes
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/tests


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.14.4-2
+ Revision: 778825
- Rebuild with proper dependencies

* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.14.4-1
+ Revision: 776599
- Import R-rtracklayer
- Import R-rtracklayer



#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-openssl
Version  : 0.9.6
Release  : 21
URL      : https://cran.r-project.org/src/contrib/openssl_0.9.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/openssl_0.9.6.tar.gz
Summary  : Toolkit for Encryption, Signatures and Certificates Based on
Group    : Development/Tools
License  : MIT
Requires: R-openssl-lib
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-testthat
BuildRequires : clr-R-helpers
BuildRequires : openssl-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-openssl package.
Group: Libraries

%description lib
lib components for the R-openssl package.


%prep
%setup -q -c -n openssl

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487769362

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1487769362
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openssl
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library openssl


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/openssl/DESCRIPTION
/usr/lib64/R/library/openssl/INDEX
/usr/lib64/R/library/openssl/LICENSE
/usr/lib64/R/library/openssl/Meta/Rd.rds
/usr/lib64/R/library/openssl/Meta/hsearch.rds
/usr/lib64/R/library/openssl/Meta/links.rds
/usr/lib64/R/library/openssl/Meta/nsInfo.rds
/usr/lib64/R/library/openssl/Meta/package.rds
/usr/lib64/R/library/openssl/Meta/vignette.rds
/usr/lib64/R/library/openssl/NAMESPACE
/usr/lib64/R/library/openssl/NEWS
/usr/lib64/R/library/openssl/R/openssl
/usr/lib64/R/library/openssl/R/openssl.rdb
/usr/lib64/R/library/openssl/R/openssl.rdx
/usr/lib64/R/library/openssl/cacert.pem
/usr/lib64/R/library/openssl/doc/bignum.R
/usr/lib64/R/library/openssl/doc/bignum.Rmd
/usr/lib64/R/library/openssl/doc/bignum.html
/usr/lib64/R/library/openssl/doc/crypto_hashing.R
/usr/lib64/R/library/openssl/doc/crypto_hashing.Rmd
/usr/lib64/R/library/openssl/doc/crypto_hashing.html
/usr/lib64/R/library/openssl/doc/index.html
/usr/lib64/R/library/openssl/doc/keys.R
/usr/lib64/R/library/openssl/doc/keys.Rmd
/usr/lib64/R/library/openssl/doc/keys.html
/usr/lib64/R/library/openssl/doc/secure_rng.R
/usr/lib64/R/library/openssl/doc/secure_rng.Rmd
/usr/lib64/R/library/openssl/doc/secure_rng.html
/usr/lib64/R/library/openssl/help/AnIndex
/usr/lib64/R/library/openssl/help/aliases.rds
/usr/lib64/R/library/openssl/help/openssl.rdb
/usr/lib64/R/library/openssl/help/openssl.rdx
/usr/lib64/R/library/openssl/help/paths.rds
/usr/lib64/R/library/openssl/html/00Index.html
/usr/lib64/R/library/openssl/html/R.css
/usr/lib64/R/library/openssl/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/openssl/libs/openssl.so

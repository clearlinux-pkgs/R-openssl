#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-openssl
Version  : 1.4
Release  : 68
URL      : https://cran.r-project.org/src/contrib/openssl_1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/openssl_1.4.tar.gz
Summary  : Toolkit for Encryption, Signatures and Certificates Based on OpenSSL
Group    : Development/Tools
License  : MIT
Requires: R-openssl-lib = %{version}-%{release}
Requires: R-askpass
BuildRequires : R-askpass
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-testthat
BuildRequires : buildreq-R
BuildRequires : openssl-dev

%description
Supports RSA, DSA and EC curves P-256, P-384, P-521, and curve25519. Cryptographic
    signatures can either be created and verified manually or via x509 certificates. 
    AES can be used in cbc, ctr or gcm mode for symmetric encryption; RSA for asymmetric
    (public key) encryption or EC for Diffie Hellman. High-level envelope functions 
    combine RSA and AES for encrypting arbitrary sized data. Other utilities include key
    generators, hash functions (md5, sha1, sha256, etc), base64 encoder, a secure random
    number generator, and 'bignum' math methods for manually performing crypto 
    calculations on large multibyte integers.

%package lib
Summary: lib components for the R-openssl package.
Group: Libraries

%description lib
lib components for the R-openssl package.


%prep
%setup -q -c -n openssl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559410750

%install
export SOURCE_DATE_EPOCH=1559410750
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openssl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openssl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openssl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/openssl/DESCRIPTION
/usr/lib64/R/library/openssl/INDEX
/usr/lib64/R/library/openssl/LICENSE
/usr/lib64/R/library/openssl/Meta/Rd.rds
/usr/lib64/R/library/openssl/Meta/features.rds
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
/usr/lib64/R/library/openssl/tests/certigo/example-elliptic-sha1.crt
/usr/lib64/R/library/openssl/tests/certigo/example-elliptic-sha1.key
/usr/lib64/R/library/openssl/tests/certigo/example-elliptic-sha1.p12
/usr/lib64/R/library/openssl/tests/certigo/example-elliptic-sha1.p7b
/usr/lib64/R/library/openssl/tests/certigo/example-leaf.crt
/usr/lib64/R/library/openssl/tests/certigo/example-leaf.p12
/usr/lib64/R/library/openssl/tests/certigo/example-leaf.p7b
/usr/lib64/R/library/openssl/tests/certigo/example-root.crt
/usr/lib64/R/library/openssl/tests/certigo/example-root.p12
/usr/lib64/R/library/openssl/tests/certigo/example-root.p7b
/usr/lib64/R/library/openssl/tests/google.dk/generate.bash
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-chain-password.p12
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-chain.p12
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-chain.pem
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-leaf.crt
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-leaf.notAfter
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-leaf.notBefore
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-leaf.sha1
/usr/lib64/R/library/openssl/tests/google.dk/wildcard-google.dk-leaf.sha256
/usr/lib64/R/library/openssl/tests/keys/authorized_keys
/usr/lib64/R/library/openssl/tests/keys/blabla.pem
/usr/lib64/R/library/openssl/tests/keys/fingerprints.txt
/usr/lib64/R/library/openssl/tests/keys/id_dsa
/usr/lib64/R/library/openssl/tests/keys/id_dsa.openssh
/usr/lib64/R/library/openssl/tests/keys/id_dsa.openssh.pw
/usr/lib64/R/library/openssl/tests/keys/id_dsa.pem
/usr/lib64/R/library/openssl/tests/keys/id_dsa.pub
/usr/lib64/R/library/openssl/tests/keys/id_dsa.pw
/usr/lib64/R/library/openssl/tests/keys/id_dsa.sshpub
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa.openssh
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa.openssh.pw
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa.pem
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa.pub
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa.pw
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa.sshpub
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384.openssh
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384.openssh.pw
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384.pem
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384.pub
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384.pw
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa384.sshpub
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521.openssh
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521.openssh.pw
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521.pem
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521.pub
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521.pw
/usr/lib64/R/library/openssl/tests/keys/id_ecdsa521.sshpub
/usr/lib64/R/library/openssl/tests/keys/id_ed25519
/usr/lib64/R/library/openssl/tests/keys/id_ed25519.openssh
/usr/lib64/R/library/openssl/tests/keys/id_ed25519.openssh.pw
/usr/lib64/R/library/openssl/tests/keys/id_ed25519.pem
/usr/lib64/R/library/openssl/tests/keys/id_ed25519.pub
/usr/lib64/R/library/openssl/tests/keys/id_ed25519.pw
/usr/lib64/R/library/openssl/tests/keys/id_ed25519.sshpub
/usr/lib64/R/library/openssl/tests/keys/id_rsa
/usr/lib64/R/library/openssl/tests/keys/id_rsa.openssh
/usr/lib64/R/library/openssl/tests/keys/id_rsa.openssh.pw
/usr/lib64/R/library/openssl/tests/keys/id_rsa.pem
/usr/lib64/R/library/openssl/tests/keys/id_rsa.pub
/usr/lib64/R/library/openssl/tests/keys/id_rsa.pw
/usr/lib64/R/library/openssl/tests/keys/id_rsa.sshpem2
/usr/lib64/R/library/openssl/tests/keys/id_rsa.sshpub
/usr/lib64/R/library/openssl/tests/keys/message
/usr/lib64/R/library/openssl/tests/keys/message.rsa.crypt
/usr/lib64/R/library/openssl/tests/keys/message.sig.dsa.sha1
/usr/lib64/R/library/openssl/tests/keys/message.sig.dsa.sha256
/usr/lib64/R/library/openssl/tests/keys/message.sig.ecdsa.sha1
/usr/lib64/R/library/openssl/tests/keys/message.sig.ecdsa.sha256
/usr/lib64/R/library/openssl/tests/keys/message.sig.ecdsa384.sha1
/usr/lib64/R/library/openssl/tests/keys/message.sig.ecdsa384.sha256
/usr/lib64/R/library/openssl/tests/keys/message.sig.ecdsa521.sha1
/usr/lib64/R/library/openssl/tests/keys/message.sig.ecdsa521.sha256
/usr/lib64/R/library/openssl/tests/keys/message.sig.ed25519.raw
/usr/lib64/R/library/openssl/tests/keys/message.sig.ed25519.sha1
/usr/lib64/R/library/openssl/tests/keys/message.sig.rsa.md5
/usr/lib64/R/library/openssl/tests/keys/message.sig.rsa.sha1
/usr/lib64/R/library/openssl/tests/keys/message.sig.rsa.sha256
/usr/lib64/R/library/openssl/tests/keys/opencpu.org.bundle
/usr/lib64/R/library/openssl/tests/keys/opencpu.org.cer
/usr/lib64/R/library/openssl/tests/keys/signatures.txt
/usr/lib64/R/library/openssl/tests/keys/testmd5.sig
/usr/lib64/R/library/openssl/tests/keys/testsha1.sig
/usr/lib64/R/library/openssl/tests/testthat.R
/usr/lib64/R/library/openssl/tests/testthat/test_bignum.R
/usr/lib64/R/library/openssl/tests/testthat/test_cert.R
/usr/lib64/R/library/openssl/tests/testthat/test_encrypt.R
/usr/lib64/R/library/openssl/tests/testthat/test_google.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash_error.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash_output_length.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash_output_value.R
/usr/lib64/R/library/openssl/tests/testthat/test_keys_dsa.R
/usr/lib64/R/library/openssl/tests/testthat/test_keys_ecdsa.R
/usr/lib64/R/library/openssl/tests/testthat/test_keys_ecdsa384.R
/usr/lib64/R/library/openssl/tests/testthat/test_keys_ecdsa521.R
/usr/lib64/R/library/openssl/tests/testthat/test_keys_ed25519.R
/usr/lib64/R/library/openssl/tests/testthat/test_keys_rsa.R
/usr/lib64/R/library/openssl/tests/testthat/test_my_key.R
/usr/lib64/R/library/openssl/tests/testthat/test_pkcs.R
/usr/lib64/R/library/openssl/tests/testthat/test_rand_error.R
/usr/lib64/R/library/openssl/tests/testthat/test_salting.R
/usr/lib64/R/library/openssl/tests/testthat/test_sodium.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/openssl/libs/openssl.so
/usr/lib64/R/library/openssl/libs/openssl.so.avx2

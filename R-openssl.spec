#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-openssl
Version  : 2.3.2
Release  : 120
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/openssl_2.3.2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/openssl_2.3.2.tar.gz
Summary  : Toolkit for Encryption, Signatures and Certificates Based on
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n openssl
pushd ..
cp -a openssl buildavx2
popd
pushd ..
cp -a openssl buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738632955

%install
export SOURCE_DATE_EPOCH=1738632955
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/openssl/tests/keys/encrypted.rsa.p7b
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
/usr/lib64/R/library/openssl/tests/keys/id_rsa.crt
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
/usr/lib64/R/library/openssl/tests/testthat/helper-version.R
/usr/lib64/R/library/openssl/tests/testthat/test_bignum.R
/usr/lib64/R/library/openssl/tests/testthat/test_cert.R
/usr/lib64/R/library/openssl/tests/testthat/test_encrypt.R
/usr/lib64/R/library/openssl/tests/testthat/test_google.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash_error.R
/usr/lib64/R/library/openssl/tests/testthat/test_hash_multihash.R
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
/usr/lib64/R/library/openssl/tests/testthat/test_ssl_ctx.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/openssl/libs/openssl.so
/V4/usr/lib64/R/library/openssl/libs/openssl.so
/usr/lib64/R/library/openssl/libs/openssl.so

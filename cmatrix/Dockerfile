FROM debian:stable
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --assume-yes build-essential autoconf curl kbd libncurses5-dev && apt-get clean
ARG VERSION=1.2
RUN curl -o /tmp/cmatrix-${VERSION}.tar.gz https://codeload.github.com/abishekvashok/cmatrix/tar.gz/${VERSION}
WORKDIR /tmp/cmatrix-${VERSION}
RUN cd /tmp && tar -C /tmp/cmatrix-${VERSION} --strip-components=1 -xzf /tmp/cmatrix-${VERSION}.tar.gz && rm /tmp/cmatrix-${VERSION}.tar.gz
RUN autoreconf -i && ./configure && make && make install
CMD ["-ba"]
ENTRYPOINT ["cmatrix"]

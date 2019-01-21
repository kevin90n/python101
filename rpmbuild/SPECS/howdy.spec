Name:   marathon
Version: 1.5.1
Release: 1.6.1
Summary: Marathon

License: Public Domain
Source0: http://downloads.mesosphere.com/marathon/v1.5.1/marathon-1.5.1.tgz
Source1: marathon.service

%description
A simple program to greet the user, Texas style.

%prep
%setup -q

%install
mkdir -p %{buildroot}/%{_bindir}
#install -p -D -m 755 bin/ %{buildroot}/bin
#install -p -D -m 755 lib/ %{buildroot}/lib
#install -p -D -m 755 %{S:1} %{buildroot}%{_initrddir}/marathon

%post
systemctl enable  marathon

%preun
if [ $1 = 0 ] ; then
systemctl stop marathon
fi

%postun
if [ "$1" -ge "1" ] ; then
#    /opt/marathon/bin/marathon --master zk://172.31.82.59:2181,172.31.82.59:2181/mesos --zk zk://172.31.82.59:2181,172.31.82.59:2181/marathon >/dev/null 2>&1
	systemctl start marathon
fi

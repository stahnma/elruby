%global major_version 1
%global minor_version 9
%global teeny_version 3
%global patch_level 392

%global major_minor_version %{major_version}.%{minor_version}

%global ruby_version %{major_minor_version}.%{teeny_version}
%global ruby_version_patch_level %{major_minor_version}.%{teeny_version}.%{patch_level}
%global ruby_abi %{major_minor_version}.1

%global ruby_archive ruby-%{ruby_version}-p%{patch_level}

%global rubygems_version 1.8.23

%global rake_version 0.9.2.2
# TODO: The IRB has strange versioning. Keep the Ruby's versioning ATM.
# http://redmine.ruby-lang.org/issues/5313
%global irb_version %{ruby_version_patch_level}
%global rdoc_version 3.9.4
%global bigdecimal_version 1.1.0
%global io_console_version 0.3
%global json_version 1.5.5
%global minitest_version 2.5.1

%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/;s/armv.*/arm/')

Summary: An interpreter of object-oriented scripting language
Name: ruby-1.9-all-in-opt
Version: %{ruby_version_patch_level}
# Note:
# As seen on perl srpm, as this (ruby) srpm contains several sub-components,
# we cannot reset the release number to 1 even when the main (ruby) version
# is updated - because it may be that the versions of sub-components don't
# change.
Release: 100%{?dist}.elruby
Group: Development/Languages
License: Ruby or BSD
URL: http://ruby-lang.org/
Source0: ftp://ftp.ruby-lang.org/pub/ruby/%{major_minor_version}/%{ruby_archive}.tar.gz
Source1: operating_system.rb

# Make mkmf verbose by default
#Patch12: ruby-1.9.3-mkmf-verbose.patch

BuildRequires: autoconf
BuildRequires: gdbm-devel
BuildRequires: ncurses-devel
BuildRequires: db4-devel
BuildRequires: libffi-devel
BuildRequires: openssl-devel
BuildRequires: libyaml-devel
BuildRequires: readline-devel
BuildRequires: tk-devel
# Needed to pass test_set_program_name(TestRubyOptions)
BuildRequires: procps

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.



%prep
%setup -q -n %{ruby_archive}

#%%patch12 -p1

%build
autoconf

./configure \
        --prefix=/opt/ruby-%{version} \
        --libdir=/opt/ruby-%{version}/lib \
        --disable-rpath \
        --enable-shared

# Q= makes the build output more verbose and allows to check Fedora
# compiler options.
make %{?_smp_mflags} COPY="cp -p" Q=


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


# Install custom operating_system.rb.
#mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
#cp %{SOURCE1} %{buildroot}%{rubygems_dir}/rubygems/defaults

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
touch %{buildroot}%{_sysconfdir}/ld.so.conf.d/ruby1.9.conf
echo "/opt/ruby-%{version}/lib" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/ruby1.9.conf

# Create folders for gem binary extensions.
mkdir -p %{buildroot}%{gem_extdir}/exts

%check
# Disable make check on ARM until the bug is fixed
# https://bugzilla.redhat.com/show_bug.cgi?id=789410
# https://bugs.ruby-lang.org/issues/6011
# same for ppc(64), RH bugzilla #803698
%ifnarch %{arm} ppc ppc64
# OpenSSL 1.0.1 is breaking the drb test suite.
# https://bugs.ruby-lang.org/issues/6221
# make check TESTS="-v -x test_drbssl.rb"
%endif

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%doc ChangeLog
%doc COPYING*
%doc doc/ChangeLog-*
%doc doc/NEWS-*
%doc GPL
%doc LEGAL
%doc NEWS
%doc README
%doc README.EXT
%doc ToDo
%lang(ja) %doc COPYING.ja
%lang(ja) %doc COPYING.ja
%lang(ja) %doc README.EXT.ja
%lang(ja) %doc README.ja
%lang(ja) %doc README.ja
/opt/ruby-%{version}
%{_sysconfdir}/ld.so.conf.d/ruby1.9.conf


%changelog
* Mon Feb 25 2013 <stahnma@fedoraproject.org> - 1.9.3.392-100
- Update for p392

* Mon Oct 29 2012 <stahnma@fedoraproject.org> - 1.9.3.286-1
- Initial build for opt

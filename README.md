# stahnma's elruby

## News

### 13 Jan 2014

I've updated the all-in-opt packages with a Ruby 2.1.0 build. The all-in-opt
packages appear to be the most popular. I imagine this is because you can just
gem install or run bundler from there. Either way, Ruby 2.1.0 is now available.
I haven't personally vetted these packages yet, if they have issues, please
file Github issues.

I also think I am going to remove the side-by-side options. This is partially
because I never finished them and also because Red Hat's software collections
seem to cover this.

## Overview

The goal of this project is to provide multiple versions and installation
methods of many MRI Rubies for Enterprise Linux (RHEL, CentOS, OEL, Scientific,
etc)

## Replacements
<hr>
These packages replace the system-provided Ruby. This means you'll be running a
ruby stack from elruby. The packages are designed to be drop-in replacements on
top of the system packages.

Upsides:

  * Everything is laid out as expected
  * Newer version of ruby available

Downsides:

  * All existing gem packages (like rubygem-whatever) may not function/install
with all versions of ruby. This may mean rebuilding gem packages or just using
`gem install`.

#### Yum Config

Ruby 1.8.7 (EL5 only)

    [elruby-replace-187]
    name="elruby replacement 1.8.7"
    baseurl="http://elruby.websages.com/replacement/1.8.7/5/$basearch/"
    enabled=1
    gpgcheck=0


Ruby 1.9.3

    [elruby-replace-193]
    name="elruby replacement 1.9.3"
    baseurl="http://elruby.websages.com/replacement/1.9.3/$releasever/$basearch/"
    enabled=1
    gpgcheck=0


Ruby 2.0.0

    [elruby-replace-200]
    name="elruby replacement 2.0.0"
    baseurl="http://elruby.websages.com/replacement/2.0.0/$releasever/$basearch/"
    enabled=1
    gpgcheck=0


## All in /opt
<hr>
These packages place everything in `/opt`. This is ideal for running ruby
application on EL. This package doesn't break out -devel, various bundled gems,
etc. This works well for bundler, and other application setups. This also has
many fewer EL specific pathces. It's really pretty close to `configure  && make
&& make install` with an `/opt` prefix.

Upsides:

  * Simple package. One package.

Downsides:

  * Binaries not in `/usr/bin`.
  * Probably won't work with other RPMs unless built specifically for this package layout.


#### Yum Config
Ruby 1.9.3

    [elruby-opt-193]
    name="elruby all-in-opt 1.9.3"
    baseurl="http://elruby.websages.com/all-in-opt/1.9.3/$releasever/$basearch/"
    enabled=1
    gpgcheck=0

 Ruby 2.0.0

    [elruby-opt-200]
    name="elruby all-in-opt 2.0.0"
    baseurl="http://elruby.websages.com/all-in-opt/2.0.0/$releasever/$basearch/"
    enabled=1
    gpgcheck=0

    [elruby-opt-210]
    name="elruby all-in-opt 2.1.0"
    baseurl="http://elruby.websages.com/all-in-opt/2.0.1/$releasever/$basearch/"
    enabled=1
    gpgcheck=0


## Side by side _WIP_
<hr>
These packages are desisgned to work side-by-side with the system-provided
ruby. These are by far the most difficult packages to produce and therefore may
lag behind the other types of packages. These are less tested as well.

Upsides:

  * Doesn't clobber system ruby.
  * Could potentially be included in EPEL someday.

Downsides:

  * bin files will be things like `/usr/bin/ruby19`
  * packages need to update dependencies etc
  * difficult to package and maintain

#### Yum Config
Ruby 1.9.3

_Still a work in progress._

_Packages not built or through QA yet_

_See News, these packages will likely be removed/never completed_


## Bugs
If you happen to find bugs, please let me know. I'll attempt to fix them. File
them at
[http://github.com/stahnma/elruby/issues](http://github.com/stahnma/elruby/issues).


## Additional Packages
I imagine if people actually start using this, they'll want more packages built
out with dependencies on these rubies. That's fine. You can file issues, or
issue a pull request on elruby and I'll try to get those built out.

Long-term I'd love to have Jenkins setup for these builds. We'll see if that happens.



## Notes
Packages are not currently signed. They will be. That's on the list.



## License
Everything in elruby is Ruby license unless otherwise noted.


## Author
[@stahnma](http://twitter.com/stahnma) on twitter. © 2013-2014

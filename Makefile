NAME=ruby
SPEC_FILE=SPECS/$(NAME).spec

RPMBUILD := $(shell if test -f /usr/bin/rpmbuild ; then echo /usr/bin/rpmbuild ; else echo "x" ; fi)

RPM_DEFINES =   --define "_specdir $(shell pwd)/SPECS" --define "_rpmdir $(shell pwd)/RPMS" --define "_sourcedir $(shell pwd)/SOURCES" --define  "_srcrpmdir $(shell pwd)/SRPMS" --define "_builddir $(shell pwd)/BUILD" --define "_source_filedigest_algorithm = 1"

MAKE_DIRS= $(shell pwd)/SPECS $(shell pwd)/SOURCES $(shell pwd)/BUILD $(shell pwd)/SRPMS $(shell pwd)/RPMS 

.PHONEY: listing listing spec uninstall

rpmcheck:
ifeq ($(RPMBUILD),x)
	$(error "rpmbuild not found, exiting...")
endif
	@mkdir -p $(MAKE_DIRS)

## use this to build an srpm locally
srpm:  rpmcheck
	@wait
	$(RPMBUILD) $(RPM_DEFINES)  -bs $(SPEC_FILE)
	@rm -rf BUILD RPMS BUILDROOT

clean:
	rm -rf BUILD SRPMS RPMS BUILDROOT *.rpm

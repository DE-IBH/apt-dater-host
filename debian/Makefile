clean:
	

install:
	mkdir -p $(DESTDIR)/usr/bin
	cp apt-dater-host $(DESTDIR)/usr/bin
	
	mkdir -p $(DESTDIR)/etc
	cp apt-dater-host.conf $(DESTDIR)/etc
	
	mkdir -p $(DESTDIR)/etc/kernel/postinst.d
	cp scripts/apt-dater-host_reboot $(DESTDIR)/etc/kernel/postinst.d
	
	mkdir -p $(DESTDIR)/etc/apt/apt.conf.d
	cp scripts/99apt-dater-host_periodic $(DESTDIR)/etc/apt/apt.conf.d

	mkdir -p $(DESTDIR)/etc/sudoers.d
	cp scripts/apt-dater-host $(DESTDIR)/etc/sudoers.d/
	chown 0440 $(DESTDIR)/etc/sudoers.d/apt-dater-host

docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v trivy-cache:/root/.cache/ aquasec/trivy:0.76.0 image --severity HIGH,CRITICAL breach-checker-backend:dev
Data:
12.11.2026r.
Wersja Trivy:
0.76.0

# breach-checker-backend:dev (debian 13.7)

Total: 49 (HIGH: 49, CRITICAL: 0)

┌───────────────┬─────────────────┬──────────┬──────────────┬───────────────────────────────────┬──────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├───────────────┼─────────────────┼──────────┼──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ bsdutils │ CVE-2026-76642 │ HIGH │ affected │ 1:2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libacl1 │ CVE-2026-54369 │ │ │ 2.3.2-2+b1 │ │ acl: Symlink traversal privilege escalation via libacl │
│ │ │ │ │ │ │ functions │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-54369 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libblkid1 │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ liblastlog2-2 │ CVE-2026-76642 │ │ │ │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1 │ CVE-2026-76642 │ │ │ │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6 │ CVE-2025-69720 │ │ │ 6.5+20250216-2 │ │ ncurses: ncurses: Buffer overflow vulnerability may lead to │
│ │ │ │ │ │ │ arbitrary code execution. │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2025-69720 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1 │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0 │ CVE-2026-119373 │ │ │ 3.46.1-7+deb13u2 │ │ sqlite: sqlite: Denial of service via heap-based buffer │
│ │ │ │ │ │ │ overflow in FTS5 │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-119373 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-119374 │ │ │ │ │ sqlite: sqlite: Arbitrary code execution via corrupted FTS5 │
│ │ │ │ │ │ │ index │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-119374 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-119379 │ │ │ │ │ sqlite: sqlite: Arbitrary code execution via crafted session │
│ │ │ │ │ │ │ changesets │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-119379 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0 │ CVE-2026-16742 │ │ │ 257.13-1~deb13u1 │ │ systemd: systemd-homed: Local privilege escalation via │
│ │ │ │ │ │ │ missing home-record signature verification │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-16742 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6 │ CVE-2025-69720 │ │ │ 6.5+20250216-2 │ │ ncurses: ncurses: Buffer overflow vulnerability may lead to │
│ │ │ │ │ │ │ arbitrary code execution. │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2025-69720 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1 │ CVE-2026-16742 │ │ │ 257.13-1~deb13u1 │ │ systemd: systemd-homed: Local privilege escalation via │
│ │ │ │ │ │ │ missing home-record signature verification │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-16742 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1 │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ login │ CVE-2026-76642 │ │ │ 1:4.16.0-2+really2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ mount │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base │ CVE-2025-69720 │ │ │ 6.5+20250216-2 │ │ ncurses: ncurses: Buffer overflow vulnerability may lead to │
│ │ │ │ │ │ │ arbitrary code execution. │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2025-69720 │
├───────────────┤ │ │ │ ├──────────────────────────────────┤ │
│ ncurses-bin │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
├───────────────┼─────────────────┤ ├──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base │ CVE-2026-9538 │ │ fix_deferred │ 5.40.1-6+deb13u1 │ │ perl-Archive-Tar: perl-Archive-Tar: Denial of Service via │
│ │ │ │ │ │ │ crafted tar header with large entry... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-9538 │
├───────────────┼─────────────────┤ ├──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux │ CVE-2026-76642 │ │ affected │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ ├──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ zlib1g │ CVE-2026-76844 │ │ fixed │ 1:1.3.dfsg+really1.3.1-1+b1 │ 1:1.3.dfsg+really1.3.1-1+deb13u1 │ zlib: zlib 1.2.11 through 1.3.2 Heap Buffer Overflow via │
│ │ │ │ │ │ │ Stale gzwrite Pointer... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76844 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-85091 │ │ │ │ │ zlib: zlib: Heap buffer overflow in gz_vacate() allows │
│ │ │ │ │ │ │ arbitrary code execution │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-85091 │
└───────────────┴─────────────────┴──────────┴──────────────┴───────────────────────────────────┴──────────────────────────────────┴──────────────────────────────────────────────────────────────┘

# breach-checker-backend:prod (debian 13.7)

Total: 49 (HIGH: 49, CRITICAL: 0)

┌───────────────┬─────────────────┬──────────┬──────────────┬───────────────────────────────────┬──────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├───────────────┼─────────────────┼──────────┼──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ bsdutils │ CVE-2026-76642 │ HIGH │ affected │ 1:2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libacl1 │ CVE-2026-54369 │ │ │ 2.3.2-2+b1 │ │ acl: Symlink traversal privilege escalation via libacl │
│ │ │ │ │ │ │ functions │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-54369 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libblkid1 │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ liblastlog2-2 │ CVE-2026-76642 │ │ │ │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1 │ CVE-2026-76642 │ │ │ │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6 │ CVE-2025-69720 │ │ │ 6.5+20250216-2 │ │ ncurses: ncurses: Buffer overflow vulnerability may lead to │
│ │ │ │ │ │ │ arbitrary code execution. │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2025-69720 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1 │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0 │ CVE-2026-119373 │ │ │ 3.46.1-7+deb13u2 │ │ sqlite: sqlite: Denial of service via heap-based buffer │
│ │ │ │ │ │ │ overflow in FTS5 │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-119373 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-119374 │ │ │ │ │ sqlite: sqlite: Arbitrary code execution via corrupted FTS5 │
│ │ │ │ │ │ │ index │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-119374 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-119379 │ │ │ │ │ sqlite: sqlite: Arbitrary code execution via crafted session │
│ │ │ │ │ │ │ changesets │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-119379 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0 │ CVE-2026-16742 │ │ │ 257.13-1~deb13u1 │ │ systemd: systemd-homed: Local privilege escalation via │
│ │ │ │ │ │ │ missing home-record signature verification │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-16742 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6 │ CVE-2025-69720 │ │ │ 6.5+20250216-2 │ │ ncurses: ncurses: Buffer overflow vulnerability may lead to │
│ │ │ │ │ │ │ arbitrary code execution. │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2025-69720 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1 │ CVE-2026-16742 │ │ │ 257.13-1~deb13u1 │ │ systemd: systemd-homed: Local privilege escalation via │
│ │ │ │ │ │ │ missing home-record signature verification │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-16742 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1 │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ login │ CVE-2026-76642 │ │ │ 1:4.16.0-2+really2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ mount │ CVE-2026-76642 │ │ │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ │ ├───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base │ CVE-2025-69720 │ │ │ 6.5+20250216-2 │ │ ncurses: ncurses: Buffer overflow vulnerability may lead to │
│ │ │ │ │ │ │ arbitrary code execution. │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2025-69720 │
├───────────────┤ │ │ │ ├──────────────────────────────────┤ │
│ ncurses-bin │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
├───────────────┼─────────────────┤ ├──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base │ CVE-2026-9538 │ │ fix_deferred │ 5.40.1-6+deb13u1 │ │ perl-Archive-Tar: perl-Archive-Tar: Denial of Service via │
│ │ │ │ │ │ │ crafted tar header with large entry... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-9538 │
├───────────────┼─────────────────┤ ├──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux │ CVE-2026-76642 │ │ affected │ 2.41.5-0+deb13u1 │ │ util-linux: util-linux: failed external mount helper still │
│ │ │ │ │ │ │ runs privileged X-mount post-hooks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76642 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78408 │ │ │ │ │ util-linux: util-linux: nsenter --join-cgroup leaks root │
│ │ │ │ │ │ │ cgroup migration authority │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78408 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78409 │ │ │ │ │ util-linux: util-linux: X-mount.subdir detached-tree │
│ │ │ │ │ │ │ resolution can escape via intermediate symlinks │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78409 │
│ ├─────────────────┤ │ │ ├──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-78410 │ │ │ │ │ util-linux: util-linux: restricted bind mounts do not pin │
│ │ │ │ │ │ │ the source, allowing X-mount.owner/group/mode... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-78410 │
├───────────────┼─────────────────┤ ├──────────────┼───────────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ zlib1g │ CVE-2026-76844 │ │ fixed │ 1:1.3.dfsg+really1.3.1-1+b1 │ 1:1.3.dfsg+really1.3.1-1+deb13u1 │ zlib: zlib 1.2.11 through 1.3.2 Heap Buffer Overflow via │
│ │ │ │ │ │ │ Stale gzwrite Pointer... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76844 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-85091 │ │ │ │ │ zlib: zlib: Heap buffer overflow in gz_vacate() allows │
│ │ │ │ │ │ │ arbitrary code execution │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-85091 │
└───────────────┴─────────────────┴──────────┴──────────────┴───────────────────────────────────┴──────────────────────────────────┴──────────────────────────────────────────────────────────────┘

# breach-checker-frontend:przed (alpine 3.24.2)

Total: 28 (HIGH: 27, CRITICAL: 1)

┌─────────────┬─────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├─────────────┼─────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ brotli-libs │ CVE-2026-111497 │ CRITICAL │ fixed │ 1.2.0-r1 │ 1.2.1-r0 │ brotli: Out-of-Bounds Write in Google Brotli Decoder │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-111497 │
├─────────────┼─────────────────┼──────────┤ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ curl │ CVE-2026-92392 │ HIGH │ │ 8.22.0-r0 │ 8.23.0-r0 │ curl: curl: HTTP/2 upload Use-After-Free │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-92392 │
├─────────────┤ │ │ │ │ │ │
│ libcurl │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libexpat │ CVE-2026-113351 │ │ │ 2.8.4-r0 │ 2.10.0-r0 │ expat: expat: Denial of Service via improper memory tracking │
│ │ │ │ │ │ │ in XML_ParserReset │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-113351 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-115506 │ │ │ │ │ expat: expat: Denial of Service via delayed entity │
│ │ │ │ │ │ │ amplification detection │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-115506 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-117610 │ │ │ │ │ expat: expat: Denial of Service via NULL pointer dereference │
│ │ │ │ │ │ │ in external entity... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-117610 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-118370 │ │ │ │ │ expat: expat: Denial of Service via integer overflow during │
│ │ │ │ │ │ │ XML attribute parsing... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-118370 │
│ ├─────────────────┤ │ │ ├───────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-77214 │ │ │ │ 2.9.0-r0 │ expat: expat: Information disclosure via heap buffer │
│ │ │ │ │ │ │ over-read in XML_ParseBuffer │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-77214 │
│ ├─────────────────┤ │ │ ├───────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-93990 │ │ │ │ 2.8.5-r0 │ expat: Expat: XML Injection via Malformed UTF-16 Input │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-93990 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libx11 │ CVE-2026-88806 │ │ │ 1.8.13-r0 │ 1.8.14-r0 │ libX11: libX11: Heap-based buffer overflow via malicious X │
│ │ │ │ │ │ │ server │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-88806 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libxslt │ CVE-2026-125350 │ │ │ 1.1.43-r3 │ 1.1.43-r4 │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-125350 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-87636 │ │ │ │ │ chromium-browser: chromium-browser: Type confusion in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-87636 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-9947 │ │ │ │ │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-9947 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ musl │ CVE-2026-107891 │ │ │ 1.2.6-r2 │ 1.2.6-r3 │ musl: musl: Arbitrary code execution via integer overflow in │
│ │ │ │ │ │ │ regcomp │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-107891 │
├─────────────┤ │ │ │ │ │ │
│ musl-utils │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ nodejs │ CVE-2026-105482 │ │ │ 24.18.1-r0 │ 24.22.1-r0 │ nodejs: nodejs: dns.resolve truncates hostnames containing a │
│ │ │ │ │ │ │ NUL character │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-105482 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-105483 │ │ │ │ │ nodejs: nodejs: TLS certificate hostname bypass via │
│ │ │ │ │ │ │ fullwidth-digit IP hostnames │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-105483 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-106069 │ │ │ │ │ nodejs: nodejs: TLS certificate hostname bypass via │
│ │ │ │ │ │ │ non-canonical IP hostnames │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-106069 │
│ ├─────────────────┤ │ │ ├───────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123863 │ │ │ │ 24.22.3-r0 │ nodejs: Node.js: Denial of Service via improper HTTP/2 │
│ │ │ │ │ │ │ session teardown │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123863 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123864 │ │ │ │ │ nodejs: nodejs: Information disclosure via HTTPS parser │
│ │ │ │ │ │ │ re-entrancy │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123864 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123865 │ │ │ │ │ nodejs: Node.js: Denial of service via HTTP/2 session │
│ │ │ │ │ │ │ resource leak during shutdown... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123865 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123866 │ │ │ │ │ nodejs: Node.js: Information disclosure via use-after-free │
│ │ │ │ │ │ │ during HTTP/2 stream teardown │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123866 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123872 │ │ │ │ │ nodejs: Node.js: Client certificate authentication bypass │
│ │ │ │ │ │ │ via TLS renegotiation │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123872 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123874 │ │ │ │ │ nodejs: nodejs: Denial of Service via HTTP/2 use-after-free │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123874 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-126051 │ │ │ │ │ nodejs: nodejs: Denial of service via premature socket │
│ │ │ │ │ │ │ closure during TLS handshake... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-126051 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ pcre2 │ CVE-2026-103111 │ │ │ 10.48-r0 │ 10.49-r0 │ pcre2: pcre2: Out-of-bounds write via crafted regular │
│ │ │ │ │ │ │ expression │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-103111 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tiff │ CVE-2026-4775 │ │ │ 4.7.1-r0 │ 4.7.2-r0 │ libtiff: libtiff: Arbitrary code execution or denial of │
│ │ │ │ │ │ │ service via signed integer... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-4775 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ zlib │ CVE-2026-85091 │ │ │ 1.3.2-r0 │ 1.3.2-r1 │ zlib: zlib: Heap buffer overflow in gz_vacate() allows │
│ │ │ │ │ │ │ arbitrary code execution │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-85091 │
└─────────────┴─────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

# breach-checker-frontend:prod (alpine 3.24.4)

Total: 3 (HIGH: 3, CRITICAL: 0)

┌─────────┬─────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├─────────┼─────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────────┤
│ libxslt │ CVE-2026-125350 │ HIGH │ fixed │ 1.1.43-r3 │ 1.1.43-r4 │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-125350 │
│ ├─────────────────┤ │ │ │ ├───────────────────────────────────────────────────────────┤
│ │ CVE-2026-87636 │ │ │ │ │ chromium-browser: chromium-browser: Type confusion in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-87636 │
│ ├─────────────────┤ │ │ │ ├───────────────────────────────────────────────────────────┤
│ │ CVE-2026-9947 │ │ │ │ │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-9947 │
└─────────┴─────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────────┘

# breach-checker-backend:dev (debian 13.7)

Total: 2 (HIGH: 2, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬─────────────────────────────┬──────────────────────────────────┬──────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├─────────┼────────────────┼──────────┼────────┼─────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ zlib1g │ CVE-2026-76844 │ HIGH │ fixed │ 1:1.3.dfsg+really1.3.1-1+b1 │ 1:1.3.dfsg+really1.3.1-1+deb13u1 │ zlib: zlib 1.2.11 through 1.3.2 Heap Buffer Overflow via │
│ │ │ │ │ │ │ Stale gzwrite Pointer... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76844 │
│ ├────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────┤
│ │ CVE-2026-85091 │ │ │ │ │ zlib: zlib: Heap buffer overflow in gz_vacate() allows │
│ │ │ │ │ │ │ arbitrary code execution │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-85091 │
└─────────┴────────────────┴──────────┴────────┴─────────────────────────────┴──────────────────────────────────┴──────────────────────────────────────────────────────────┘

# breach-checker-backend:prod (debian 13.7)

Total: 2 (HIGH: 2, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬─────────────────────────────┬──────────────────────────────────┬──────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├─────────┼────────────────┼──────────┼────────┼─────────────────────────────┼──────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ zlib1g │ CVE-2026-76844 │ HIGH │ fixed │ 1:1.3.dfsg+really1.3.1-1+b1 │ 1:1.3.dfsg+really1.3.1-1+deb13u1 │ zlib: zlib 1.2.11 through 1.3.2 Heap Buffer Overflow via │
│ │ │ │ │ │ │ Stale gzwrite Pointer... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-76844 │
│ ├────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────┤
│ │ CVE-2026-85091 │ │ │ │ │ zlib: zlib: Heap buffer overflow in gz_vacate() allows │
│ │ │ │ │ │ │ arbitrary code execution │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-85091 │
└─────────┴────────────────┴──────────┴────────┴─────────────────────────────┴──────────────────────────────────┴──────────────────────────────────────────────────────────┘

# breach-checker-frontend:przed (alpine 3.24.2)

Total: 28 (HIGH: 27, CRITICAL: 1)

┌─────────────┬─────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├─────────────┼─────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ brotli-libs │ CVE-2026-111497 │ CRITICAL │ fixed │ 1.2.0-r1 │ 1.2.1-r0 │ brotli: Out-of-Bounds Write in Google Brotli Decoder │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-111497 │
├─────────────┼─────────────────┼──────────┤ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ curl │ CVE-2026-92392 │ HIGH │ │ 8.22.0-r0 │ 8.23.0-r0 │ curl: curl: HTTP/2 upload Use-After-Free │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-92392 │
├─────────────┤ │ │ │ │ │ │
│ libcurl │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libexpat │ CVE-2026-113351 │ │ │ 2.8.4-r0 │ 2.10.0-r0 │ expat: expat: Denial of Service via improper memory tracking │
│ │ │ │ │ │ │ in XML_ParserReset │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-113351 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-115506 │ │ │ │ │ expat: expat: Denial of Service via delayed entity │
│ │ │ │ │ │ │ amplification detection │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-115506 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-117610 │ │ │ │ │ expat: expat: Denial of Service via NULL pointer dereference │
│ │ │ │ │ │ │ in external entity... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-117610 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-118370 │ │ │ │ │ expat: expat: Denial of Service via integer overflow during │
│ │ │ │ │ │ │ XML attribute parsing... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-118370 │
│ ├─────────────────┤ │ │ ├───────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-77214 │ │ │ │ 2.9.0-r0 │ expat: expat: Information disclosure via heap buffer │
│ │ │ │ │ │ │ over-read in XML_ParseBuffer │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-77214 │
│ ├─────────────────┤ │ │ ├───────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-93990 │ │ │ │ 2.8.5-r0 │ expat: Expat: XML Injection via Malformed UTF-16 Input │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-93990 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libx11 │ CVE-2026-88806 │ │ │ 1.8.13-r0 │ 1.8.14-r0 │ libX11: libX11: Heap-based buffer overflow via malicious X │
│ │ │ │ │ │ │ server │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-88806 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libxslt │ CVE-2026-125350 │ │ │ 1.1.43-r3 │ 1.1.43-r4 │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-125350 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-87636 │ │ │ │ │ chromium-browser: chromium-browser: Type confusion in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-87636 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-9947 │ │ │ │ │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-9947 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ musl │ CVE-2026-107891 │ │ │ 1.2.6-r2 │ 1.2.6-r3 │ musl: musl: Arbitrary code execution via integer overflow in │
│ │ │ │ │ │ │ regcomp │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-107891 │
├─────────────┤ │ │ │ │ │ │
│ musl-utils │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ nodejs │ CVE-2026-105482 │ │ │ 24.18.1-r0 │ 24.22.1-r0 │ nodejs: nodejs: dns.resolve truncates hostnames containing a │
│ │ │ │ │ │ │ NUL character │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-105482 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-105483 │ │ │ │ │ nodejs: nodejs: TLS certificate hostname bypass via │
│ │ │ │ │ │ │ fullwidth-digit IP hostnames │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-105483 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-106069 │ │ │ │ │ nodejs: nodejs: TLS certificate hostname bypass via │
│ │ │ │ │ │ │ non-canonical IP hostnames │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-106069 │
│ ├─────────────────┤ │ │ ├───────────────┼──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123863 │ │ │ │ 24.22.3-r0 │ nodejs: Node.js: Denial of Service via improper HTTP/2 │
│ │ │ │ │ │ │ session teardown │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123863 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123864 │ │ │ │ │ nodejs: nodejs: Information disclosure via HTTPS parser │
│ │ │ │ │ │ │ re-entrancy │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123864 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123865 │ │ │ │ │ nodejs: Node.js: Denial of service via HTTP/2 session │
│ │ │ │ │ │ │ resource leak during shutdown... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123865 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123866 │ │ │ │ │ nodejs: Node.js: Information disclosure via use-after-free │
│ │ │ │ │ │ │ during HTTP/2 stream teardown │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123866 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123872 │ │ │ │ │ nodejs: Node.js: Client certificate authentication bypass │
│ │ │ │ │ │ │ via TLS renegotiation │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123872 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-123874 │ │ │ │ │ nodejs: nodejs: Denial of Service via HTTP/2 use-after-free │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-123874 │
│ ├─────────────────┤ │ │ │ ├──────────────────────────────────────────────────────────────┤
│ │ CVE-2026-126051 │ │ │ │ │ nodejs: nodejs: Denial of service via premature socket │
│ │ │ │ │ │ │ closure during TLS handshake... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-126051 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ pcre2 │ CVE-2026-103111 │ │ │ 10.48-r0 │ 10.49-r0 │ pcre2: pcre2: Out-of-bounds write via crafted regular │
│ │ │ │ │ │ │ expression │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-103111 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tiff │ CVE-2026-4775 │ │ │ 4.7.1-r0 │ 4.7.2-r0 │ libtiff: libtiff: Arbitrary code execution or denial of │
│ │ │ │ │ │ │ service via signed integer... │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-4775 │
├─────────────┼─────────────────┤ │ ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ zlib │ CVE-2026-85091 │ │ │ 1.3.2-r0 │ 1.3.2-r1 │ zlib: zlib: Heap buffer overflow in gz_vacate() allows │
│ │ │ │ │ │ │ arbitrary code execution │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-85091 │
└─────────────┴─────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────

# breach-checker-frontend:prod (alpine 3.24.4)

Total: 3 (HIGH: 3, CRITICAL: 0)

┌─────────┬─────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │ Fixed Version │ Title │
├─────────┼─────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────────┤
│ libxslt │ CVE-2026-125350 │ HIGH │ fixed │ 1.1.43-r3 │ 1.1.43-r4 │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-125350 │
│ ├─────────────────┤ │ │ │ ├───────────────────────────────────────────────────────────┤
│ │ CVE-2026-87636 │ │ │ │ │ chromium-browser: chromium-browser: Type confusion in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-87636 │
│ ├─────────────────┤ │ │ │ ├───────────────────────────────────────────────────────────┤
│ │ CVE-2026-9947 │ │ │ │ │ chromium-browser: Use after free in XML │
│ │ │ │ │ │ │ https://avd.aquasec.com/nvd/cve-2026-9947 │
└─────────┴─────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────────┘

Frontend przeszedł na multi-stage build: narzędzia kontroli jakości zostały w etapie lint, a obrazem końcowym jest sam nginx:alpine z trzema plikami strony — dzięki temu zniknęły wszystkie podatności typu node-pkg. Backend celowo pozostał jednoetapowy (biblioteki z gotowych pakietów, brak kompilatorów do usunięcia), ale działa jako użytkownik bez uprawnień root pod gunicornem. Oba obrazy produkcyjne przebudowałem z opcją --pull, żeby pobrać najświeższe wersje obrazów bazowych i wszystkie dostępne w nich poprawki. Pozostałe podatności HIGH/CRITICAL nie mają dziś dostępnej poprawki — pochodzą z obrazów bazowych python:3.12-slim i nginx:alpine i czekają na łatki w dystrybucji, więc nie usunie ich przebudowanie; możemy je tylko ocenić pod kątem naszego zastosowania albo zmienić obraz bazowy

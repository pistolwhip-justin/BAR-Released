# BAR-Released

A release wrapper for building and distributing an installable APK of [BAR (Basic Audio Recorder)](https://github.com/PatrykMis/BAR).

## Download

**[Open Releases and download BAR-1.0.0-debug.apk](https://github.com/pistolwhip-justin/BAR-Released/releases)**

## Build and release process

- The authoritative application source remains upstream at [PatrykMis/BAR](https://github.com/PatrykMis/BAR).
- GitHub Actions checks out upstream source at fixed commit `4b6a49ab3e53e1862bd49f07ac4007c1cba8af5e`.
- Actions uses JDK 25 and the upstream Gradle wrapper to run `./gradlew build --no-daemon`.
- The debug APK and its SHA-256 checksum are attached directly to the versioned GitHub Release.
- The workflow refuses to overwrite an existing release. A release containing the expected APK is left unchanged; an incomplete release fails for investigation.
- The APK is not committed to the source tree.

## Install and device validation

This is a debug/sideloading APK, not a production or Play Store build. Its debug application ID is `com.patrykmis.bar.debug`.

Download the APK from Releases, install it on Android, grant microphone and notification permissions, and add the recording tile to Quick Settings.

A successful CI build does not prove installation or physical-device behavior. On the target phone, validate the tile, persistent notification, background recording, output-file creation, and audio format.

## Upstream project and license

BAR is maintained upstream by Patryk Miś and contributors. This repository does not claim ownership of the application source. BAR is licensed under **GPL-3.0-only**; see the [upstream license](https://github.com/PatrykMis/BAR/blob/master/LICENSE) and preserve its notices.

## Reproducibility

The source revision is pinned in `.github/workflows/release-1.0.0.yml`. A future upstream version should get a new versioned workflow and release, not replace the source revision or assets of an existing release.

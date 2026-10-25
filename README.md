# BAR-Released

A release wrapper for building and distributing installable APKs of [BAR (Basic Audio Recorder)](https://github.com/PatrykMis/BAR).

## Download

**[Open Releases and download the latest APK](https://github.com/pistolwhip-justin/BAR-Released/releases)**

- **v1.0.0:** initial upstream build.
- **v1.0.1:** adds a Stop action to the persistent recording notification (pending build and device validation).

## Build and release process

- The authoritative application source remains upstream at [PatrykMis/BAR](https://github.com/PatrykMis/BAR).
- Each versioned workflow checks out upstream source at fixed commit `4b6a49ab3e53e1862bd49f07ac4007c1cba8af5e`.
- Version-specific local patches are maintained in this repository and applied reproducibly before building. The notification Stop-action patch is in `scripts/apply-notification-stop-patch.py`.
- Actions uses JDK 25 and the upstream Gradle wrapper to run `./gradlew build --no-daemon`.
- The debug APK and its SHA-256 checksum are attached directly to the corresponding versioned GitHub Release.
- Workflows refuse to overwrite an existing release. A release containing the expected APK is left unchanged; an incomplete release fails for investigation.
- APKs are not committed to the source tree.

## Install and device validation

These are debug/sideloading APKs, not production or Play Store builds. The debug application ID is `com.patrykmis.bar.debug`.

Download an APK from Releases, install it on Android, grant microphone and notification permissions, and add the recording tile to Quick Settings.

A successful CI build does not prove installation or physical-device behavior. For v1.0.1, specifically test Start, Pause, Resume, Stop while recording, Stop while paused, microphone indicator/access ending, saved file in the selected directory, selected audio format, and the Quick Settings tile state.

## Upstream project and license

BAR is maintained upstream by Patryk Miś and contributors. This repository does not claim ownership of the application source. BAR is licensed under **GPL-3.0-only**; see the [upstream license](https://github.com/PatrykMis/BAR/blob/master/LICENSE) and preserve its notices.

## Reproducibility

Each version has its own workflow and release. Do not replace the source revision or assets of an existing release; publish fixes as a new patch version.

# Bar Released

Bar Released is a branded, installable release of the open-source recorder based on [upstream BAR](https://github.com/PatrykMis/BAR).

## Download

**[Open Releases and download the latest APK](https://github.com/pistolwhip-justin/BAR-Released/releases)**

- **v1.0.0:** initial upstream build.
- **v1.0.1:** adds a Stop action to the persistent recording notification; physical-device test passed.
- **v1.0.2:** renames the app to Bar Released in the Android UI and release-facing documentation while retaining the existing package ID and Stop-action fix.

## Build and release process

- The authoritative application source remains upstream at [PatrykMis/BAR](https://github.com/PatrykMis/BAR); this repository maintains reproducible local patches for the distributed Bar Released build.
- Each versioned workflow checks out upstream source at fixed commit `4b6a49ab3e53e1862bd49f07ac4007c1cba8af5e`.
- Version-specific patches are maintained in this repository and applied reproducibly before building: `scripts/apply-notification-stop-patch.py` adds the notification Stop action and `scripts/apply-bar-released-branding.py` applies the Bar Released name and v1.0.2 version metadata.
- GitHub Actions uses JDK 25 and the upstream Gradle wrapper to run `./gradlew build --no-daemon`.
- The debug APK and its SHA-256 checksum are attached directly to the corresponding versioned GitHub Release.
- Workflows refuse to overwrite an existing release. A release containing the expected APK is left unchanged; an incomplete release fails for investigation.
- APKs are not committed to the source tree.

## Install and device validation

These are debug/sideloading APKs, not production or Play Store builds. The debug application ID remains `com.patrykmis.bar.debug` so the app's Android identity is preserved.

Download an APK from Releases, install it on Android, grant microphone and notification permissions, and add the recording tile to Quick Settings.

The v1.0.1 Stop-action behavior passed a physical-device test. For v1.0.2, confirm the launcher/app settings display name is **Bar Released** and do a brief regression check of Start, Pause, Resume, Stop, microphone access ending, and saved-file creation. CI success alone does not prove physical-device behavior.

## Upstream project and license

The upstream recorder is maintained by Patryk Miś and contributors. Bar Released does not claim ownership of that upstream source. Upstream BAR is licensed under **GPL-3.0-only**; see the [upstream license](https://github.com/PatrykMis/BAR/blob/master/LICENSE) and preserve its notices.

## Reproducibility

Each version has its own workflow and release. Do not replace the source revision or assets of an existing release; publish changes as a new patch version.
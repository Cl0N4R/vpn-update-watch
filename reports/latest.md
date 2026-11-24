# گزارش پایش نسخه‌ها

آخرین بررسی (UTC): 2026-11-24T20:17:34.232537+00:00

> فقط داده‌های رسمی GitHub گزارش می‌شود؛ این ابزار درباره نصب یا ارتقا توصیه نمی‌کند.

## BPB VPN — `bia-pain-bache/BPB-VPN`
### BPB 1.3.0 (Stable)
- Tag: `v1.3.0`
- تاریخ انتشار: 2026-11-21T15:03:35Z
- صفحه رسمی: https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.3.0
- APKهای ARM64:
  - [bpb-1.3.0-arm64-v8a.apk](https://github.com/bia-pain-bache/BPB-VPN/releases/download/v1.3.0/bpb-1.3.0-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
# BPB VPN v1.3.0

This release introduces some important improvements like VLESS DNS compatibility and improvements, fallback DNS servers while using Exit Nodes and also supporting **SSH** connection for users who are not familiar with complicated VPS setups.

## 🌟 SSH protocol

Along with providing free private solutions for a wide range of users, I added this protocol to empower amateur users who have no knowledge of server configurations. It allows them to simply purchase a VPS in an emergency and connect via SSH with zero setup.  
Right now SSH proxies endure more than some modern protocols like reality on some ISPs in Iran for low bandwidth connections.  
It should be mentioned that SSH protocol only supports TCP traffic and you won't be able to use Telegram calls, Clubhouse etc.

## 🌟 Global Remote DNS

Merged all protocols' **Remote DNS** servers into one field in Global settings. VLESS now supports Cloudflare DNS servers and hijacks them into related DoH servers within worker.  
The Remote DNS only accepts IPv4 and IPv6 now to boost up performance specially for **VLESS**.

> [!IMPORTANT]
> The worker scripts get updated in the background after you update to this version. however it needs to connect to the internet, You can confirm worker update by checking `Settings` > `VLESS` > `Cloudflare accounts`, there will be a manual update button in case the update was not successful.

## 💡 Bug fixes and improvements

- Added SSH protocol as it needs zero configuration skills for amateur users, supporting password, SSH key methods and Keep Alive settings.
- Enabled Psiphon, Tor and Chain proxy (except WireGuard and Hysteria2) for SSH connection.
- Made Remote DNS global, improved VLESS DNS performance and added Cloudflare DNS support to.
- Added Tor and Psiphon DNS servers as a fallback to Remote DNS.
- Added theme to config view page.
- Added config download button.
- Updated Log view page UI and added search box to it.
- Updated worker minification setup.
- Refactored the core logic.
- Fixed Tor and Psiphon routing bug in 1.2.2.
- Fixed scanner pause bug.
- Fixed log view lag.

**Full Changelog**: https://github.com/bia-pain-bache/BPB-VPN/compare/v1.2.1...v1.3.0

![GitHub Downloads (all assets, specific tag)](https://img.shields.io/github/downloads/bia-pain-bache/BPB-VPN/v1.3.0/total)


### BPB 1.2.2 (Pre-release)
- Tag: `v1.2.2`
- تاریخ انتشار: 2026-11-20T14:21:07Z
- صفحه رسمی: https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.2.2
- APKهای ARM64:
  - [bpb-1.2.2-arm64-v8a.apk](https://github.com/bia-pain-bache/BPB-VPN/releases/download/v1.2.2/bpb-1.2.2-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
# 🌟 Global Remote DNS

Merged all protocols' **Remote DNS** servers into one field in Global settings. VLESS now supports Cloudflare DNS servers and hijacks them into related DoH servers within worker.  
The Remote DNS only accepts IPv4 and IPv6 now to boost up performance specially for **VLESS**.

> [!IMPORTANT]
> The worker scripts get updated in the background after you update to this version. however it needs to connect to the internet, You can confirm worker update by checking `Settings` > `VLESS` > `Cloudflare accounts`, there will be a manual update button in case the update was not successful.

## 💡 Bug fixes and improvements

- Made Remote DNS global, improved VLESS DNS performance and added Cloudflare DNS support to.
- Updated worker minification setup.
- Fixed scanner pause bug.

**Full Changelog**: https://github.com/bia-pain-bache/BPB-VPN/compare/v1.2.1...v1.2.2

![GitHub Downloads (all assets, specific tag)](https://img.shields.io/github/downloads/bia-pain-bache/BPB-VPN/v1.2.2/total)


### BPB 1.2.1 (Stable)
- Tag: `v1.2.1`
- تاریخ انتشار: 2026-11-18T13:12:17Z
- صفحه رسمی: https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.2.1
- APKهای ARM64:
  - [bpb-1.2.1-arm64-v8a.apk](https://github.com/bia-pain-bache/BPB-VPN/releases/download/v1.2.1/bpb-1.2.1-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
# 💡 Bug fixes and Improvements

- Made some revisions to **Domain Fronting** config to fix DNS issues and TLS repacks.
- Set default Per-app page behaviour to show system apps (slower but more convinient). #17
- Fixed Region selection UI bug when Android nav bar is enabled.
- Renamed **Worker** connection type to **VLESS** to fit settings' sections.

> [!IMPORTANT]
> Some default settings have been changed since 1.0.0 and 1.1.0, so I recommend to reset settings after this update just to be sure. Don't worry, this will preserve your clean IPs and endpoints.

**Full Changelog**: https://github.com/bia-pain-bache/BPB-VPN/compare/v1.2.0...v1.2.1

![GitHub Downloads (all assets, specific tag)](https://img.shields.io/github/downloads/bia-pain-bache/BPB-VPN/v1.2.1/total)


### BPB 1.2.0 (Stable)
- Tag: `v1.2.0`
- تاریخ انتشار: 2026-11-15T14:18:14Z
- صفحه رسمی: https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.2.0
- APKهای ARM64:
  - [bpb-1.2.0-arm64-v8a.apk](https://github.com/bia-pain-bache/BPB-VPN/releases/download/v1.2.0/bpb-1.2.0-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
# 🎉 BPB VPN is here

Welcome to BPB VPN, a companion app designed to make setting up and using the BPB Panel and Wizard simpler and more approachable. From getting started to managing your VPN connection and even combining it with third-party proxies like Tor and Psiphon, my goal is to make the experience easier to follow and less of a hassle.

## 🌟 BPB Cloudflare scanners

BPB is now equipped with specific Cloudflare scanners for all protocol! The scanner follows user settings for protocol i.e. Fingerprint, SNI, IP version, Custom domain, Transport and is even capable of scanning with Fragment and UDP Obfuscation (ECH is excluded). Please note that the more `Probes count` you set, the better IPs you get, but the downside is the scanner consumes more worker requests during VLESS scanning.

## 🌟 Serverless DNS mode

We've already seen DNS clients like `Rethink`, now assume you have a full DNS client with traffic splitting and even DNS tester!
A very helpful feature which helps you through DNS disruptions supporting UDP,TCP,DoH and DoQ servers. You have your Workers and Pages DoH as private servers (using Cloudflare Security DoH as backend) along with some well-known public DNS servers of all types.

The lovely part of this feature is **Fake SNI servers**, it uses Cloudflare, Google and Quad9 DoH servers with a Fake whitelisted SNI.

## 💡 Bug fixes and Improvements

- Added **Snowflake AMP** to Tor modes.
- Added **Routing Strategy**.
- **Connection behaviour:** The app now checks the actual connection before updating the UI. As a result, connections that are not working remain in the `Connecting` state, unlike the usual behavior in v2rayNG and similar apps.
- Renamed **Serverless Fragment** to **Serverless Packet**, since it also supports UDP obfuscation.
- Updated the default **UDP obfuscation** noises to simulate the AmneziaWG obfuscation.
- Added **QUIC**, **DNS query**, **STUN Binding** mimic presets to UDP noises, along with a **None** mode to apply custom packet for **Expression** UDP noise mode.
- Changed the default Warp **Reserved bytes** value to disabled to reduce protocol fingerprinting on some ISPs.
- Added bilingual Github issue templates in Farsi and English. It worth mentioning that all BPB projects are handled by one person, so please only report technical bugs and misconfigurations (not the app performance on your ISP) with all requested info, issue gets closed ASAP otherwise.
- Updated **Reset settings** behaviour so that clean IPs and endpoints are preserved.
- Updated the **Domain Fronting** + **Psiphon** config, it has much better performance now and tries to keep [@Patterniha](https://github.com/patterniha) template safe.
- Updated the routing rules to block Iran firewall IPs by default.
- Updated Xray-core to v26.11.9
- Updated Tor to v4.9.16
- Added ECH retries to Cloudflare API calls.
- Added **Serverless DNS** mode supporting UDP,TCP,DoH and DoQ servers. Private servers use Cloudflare Security DoH as backend.
- Added **Prefer IPv6** option.
- Updated routing rules.
- Added Fake SNI DoH feat. to DNS mode.
- Updated Fragment default setting, for now it may works on some ISPs.
- Fixed the BPB quick settings tile bug #9
- Fixed UI and documentation bugs #13 #14

> [!IMPORTANT]
> Some default settings have been changed since 1.0.0 and 1.1.0, so I recommend to reset settings after this update just to be sure. Don't worry, this will preserve your clean IPs and endpoints.

**Full Changelog**: https://github.com/bia-pain-bache/BPB-VPN/compare/v1.0.0...v1.2.0

![GitHub Downloads (all assets, specific tag)](https://img.shields.io/github/downloads/bia-pain-bache/BPB-VPN/v1.2.0/total)


### BPB 1.1.0 (Pre-release)
- Tag: `v1.1.0`
- تاریخ انتشار: 2026-11-11T15:35:25Z
- صفحه رسمی: https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.1.0
- APKهای ARM64:
  - [bpb-1.1.0-arm64-v8a.apk](https://github.com/bia-pain-bache/BPB-VPN/releases/download/v1.1.0/bpb-1.1.0-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
# 🎉 BPB VPN is here

Welcome to BPB VPN, a companion app designed to make setting up and using the BPB Panel and Wizard simpler and more approachable. From getting started to managing your VPN connection and even combining it with third-party proxies like Tor and Psiphon, my goal is to make the experience easier to follow and less of a hassle.

## 🌟 BPB Cloudflare scanners

BPB is now equipped with specific Cloudflare scanners for all protocol! The scanner follows user settings for protocol i.e. Fingerprint, SNI, IP version, Custom domain, Transport and is even capable of scanning with Fragment and UDP Obfuscation (ECH is excluded). Please note that the more `Probes count` you set, the better IPs you get, but the downside is the scanner consumes more worker requests during VLESS scanning.

## 💡 Bug fixes and Improvements

- Added **Snowflake AMP** to Tor modes.
- Added **Routing Strategy**.
- **Connection behaviour:** The app now checks the actual before updating the UI. As a result, connections that are not working remain in the `Connecting` state, unlike the usual behavior in v2rayNG and similar apps.
- Renamed **Serverless Fragment** to **Serverless Packet**, since it also supports UDP obfuscation.
- Updated the default **UDP obfuscation** noises to simulate the AmneziaWG obfuscation.
- Added **QUIC**, **DNS query**, **STUN Binding** mimic presets to UDP noises, along with a **None** mode to apply custom packet for **Expression** UDP noise mode.
- Changed the default Warp **Reserved bytes** value to disabled to reduce protocol fingerprinting on some ISPs.
- Added bilingual Github issue templates in Farsi and English. It worth mentioning that all BPB projects are handled by one person, so please only report technical bugs and misconfigurations (not the app performance on your ISP) with all requested info, issue gets closed ASAP otherwise.
- Updated **Reset settings** behaviour so that clean IPs and endpoints are preserved.
- Updated the **Domain Fronting** + **Psiphon** config, it has much better performance now and tries to keep [@Patterniha](https://github.com/patterniha) template safe.
- Updated the routing rules to block Iran firewall IPs by default.
- Updated Xray-core to v26.11.9
- Updated Tor to v4.9.16
- Fixed the BPB quick settings tile bug #9

![GitHub Downloads (all assets, specific tag)](https://img.shields.io/github/downloads/bia-pain-bache/BPB-VPN/v1.1.0/total)


## PattNG — `patterniha/PattNG`
### PattNG v2.4.0-P74 (Stable)
- Tag: `2.4.0-P74`
- تاریخ انتشار: 2026-11-23T05:00:11Z
- صفحه رسمی: https://github.com/patterniha/PattNG/releases/tag/2.4.0-P74
- APKهای ARM64:
  - [PattNG_2.4.0-P74_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.4.0-P74/PattNG_2.4.0-P74_arm64-v8a.apk)
  - [PattNG_fdroid_2.4.0-P74_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.4.0-P74/PattNG_fdroid_2.4.0-P74_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
.

### PattNG v2.4.0-P73 (Stable)
- Tag: `2.4.0-P73`
- تاریخ انتشار: 2026-11-17T01:24:25Z
- صفحه رسمی: https://github.com/patterniha/PattNG/releases/tag/2.4.0-P73
- APKهای ARM64:
  - [PattNG_2.4.0-P73_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.4.0-P73/PattNG_2.4.0-P73_arm64-v8a.apk)
  - [PattNG_fdroid_2.4.0-P73_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.4.0-P73/PattNG_fdroid_2.4.0-P73_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
.

### PattNG v2.4.0-P72 (Stable)
- Tag: `2.4.0-P72`
- تاریخ انتشار: 2026-11-14T01:13:36Z
- صفحه رسمی: https://github.com/patterniha/PattNG/releases/tag/2.4.0-P72
- APKهای ARM64:
  - [PattNG_2.4.0-P72_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.4.0-P72/PattNG_2.4.0-P72_arm64-v8a.apk)
  - [PattNG_fdroid_2.4.0-P72_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.4.0-P72/PattNG_fdroid_2.4.0-P72_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
.

### PattNG v2.3.15-P71 (Stable)
- Tag: `2.3.15-P71`
- تاریخ انتشار: 2026-11-01T11:02:05Z
- صفحه رسمی: https://github.com/patterniha/PattNG/releases/tag/2.3.15-P71
- APKهای ARM64:
  - [PattNG_2.3.15-P71_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.3.15-P71/PattNG_2.3.15-P71_arm64-v8a.apk)
  - [PattNG_fdroid_2.3.15-P71_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.3.15-P71/PattNG_fdroid_2.3.15-P71_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
.

### PattNG v2.3.13-P70 (Stable)
- Tag: `2.3.13-P70`
- تاریخ انتشار: 2026-10-27T21:01:41Z
- صفحه رسمی: https://github.com/patterniha/PattNG/releases/tag/2.3.13-P70
- APKهای ARM64:
  - [PattNG_2.3.13-P70_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.3.13-P70/PattNG_2.3.13-P70_arm64-v8a.apk)
  - [PattNG_fdroid_2.3.13-P70_arm64-v8a.apk](https://github.com/patterniha/PattNG/releases/download/2.3.13-P70/PattNG_fdroid_2.3.13-P70_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
.

## Karing — `KaringX/karing`
### v1.2.26.2934 (Stable)
- Tag: `v1.2.26.2934`
- تاریخ انتشار: 2026-11-19T03:17:40Z
- صفحه رسمی: https://github.com/KaringX/karing/releases/tag/v1.2.26.2934
- APKهای ARM64:
  - [karing_1.2.26.2934_android_arm64-v8a.apk](https://github.com/KaringX/karing/releases/download/v1.2.26.2934/karing_1.2.26.2934_android_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
1. Fixed a crash occurring in the core.
2. Windows: Renamed the environment variable `ENABLE_IMPELLER` to `KARING_ENABLE_IMPELLER` to avoid conflicts.
3. Improved automatic update checks: if the check via the primary domain fails, the application will now attempt to use a backup domain.

iOS/tvOS AppStore: (Search Keywords: karing vpn) https://apps.apple.com/us/app/karing/id6472431552

### v1.2.26.2933 (Stable)
- Tag: `v1.2.26.2933`
- تاریخ انتشار: 2026-11-17T04:50:59Z
- صفحه رسمی: https://github.com/KaringX/karing/releases/tag/v1.2.26.2933
- APKهای ARM64:
  - [karing_1.2.26.2933_android_arm64-v8a.apk](https://github.com/KaringX/karing/releases/download/v1.2.26.2933/karing_1.2.26.2933_android_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
1. Windows: Fixed an issue where the third-party dependency `permission_handler` caused problems when retrieving the current location #2114
2. Windows: Improved the addition of firewall rules (rules are now added only when running with administrator privileges)
3. Linux: Fixed an issue where the tray menu would not appear #2082
4. Android: Fixed an exception in `WidgetsAppState._onUnknownRoute`
5. Added compatibility for `extra=null` in VLESS #2115

iOS/tvOS AppStore: (Search Keywords: karing vpn) https://apps.apple.com/us/app/karing/id6472431552

### v1.2.26.2932 (Stable)
- Tag: `v1.2.26.2932`
- تاریخ انتشار: 2026-11-16T03:42:41Z
- صفحه رسمی: https://github.com/KaringX/karing/releases/tag/v1.2.26.2932
- APKهای ARM64:
  - [karing_1.2.26.2932_android_arm64-v8a.apk](https://github.com/KaringX/karing/releases/download/v1.2.26.2932/karing_1.2.26.2932_android_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
1. Core: Log improvements #2103
2. Windows: Crash information is no longer collected for `KaringService` when launched by third-party applications.
3. Recompiled the core to address potential false-positive detections by certain antivirus software #2109 #2100
4. Fixed an issue where editing WireGuard (WG) configurations could trigger an exception. #2101
5. Windows: Added a new system environment variable, `ENABLE_IMPELLER`, to enable the Flutter Impeller engine (set `ENABLE_IMPELLER` to 1). Users experiencing a black screen on Windows may try adding this environment variable #2099 #2106

iOS/tvOS AppStore: (Search Keywords: karing vpn) https://apps.apple.com/us/app/karing/id6472431552

### v1.2.26.2931 (Stable)
- Tag: `v1.2.26.2931`
- تاریخ انتشار: 2026-11-13T12:03:34Z
- صفحه رسمی: https://github.com/KaringX/karing/releases/tag/v1.2.26.2931
- APKهای ARM64:
  - [karing_1.2.26.2931_android_arm64-v8a.apk](https://github.com/KaringX/karing/releases/download/v1.2.26.2931/karing_1.2.26.2931_android_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
1. Fixed an issue where performing an profile "auto-update" or "update all" profile could cause certain profile settings to be reset #2098
2. Core: Improved resource usage for WireGuard
3. Core: Improved certain log entries
4. Fixed an issue where DNS rules appeared empty under "Network Check"
5. Fixed an issue where domains for certain types of nodes were not being added to `dns_outbound_out`

iOS/tvOS AppStore: (Search Keywords: karing vpn) https://apps.apple.com/us/app/karing/id6472431552

### v1.2.26.2930 (Stable)
- Tag: `v1.2.26.2930`
- تاریخ انتشار: 2026-11-13T04:56:36Z
- صفحه رسمی: https://github.com/KaringX/karing/releases/tag/v1.2.26.2930
- APKهای ARM64:
  - [karing_1.2.26.2930_android_arm64-v8a.apk](https://github.com/KaringX/karing/releases/download/v1.2.26.2930/karing_1.2.26.2930_android_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
1. Fixed issues where certain fields were omitted during protocol conversion.
2. Switched to an `endpoint` structure for storing WireGuard configurations (both newly added and manually edited), and added support for editing peers.
3. Added support for `hy2: obfs - gecko` conversion (#2097).


iOS/tvOS AppStore: (Search Keywords: karing vpn) https://apps.apple.com/us/app/karing/id6472431552

## MLM VPN — `mlmvpn/mlmvpn_android`
### v1.2.49 — گروه‌های لحظه‌ای مثل تلگرام، خبر پاسخ و سنجاق، و اینترنت و باتری کمتر در گره (Stable)
- Tag: `v1.2.49`
- تاریخ انتشار: 2026-11-11T22:51:33Z
- صفحه رسمی: https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.49
- APKهای ARM64:
  - [mlmvpn-1.2.49-arm64-v8a-release.apk](https://github.com/mlmvpn/mlmvpn_android/releases/download/v1.2.49/mlmvpn-1.2.49-arm64-v8a-release.apk)

**یادداشت توسعه‌دهنده:**
## گروه‌های لحظه‌ای مثل تلگرام، خبر پاسخ و سنجاق، و اینترنت و باتری کمتر در گره

### افزوده‌شده
- **گره: گروه‌ها و کانال‌ها لحظه‌ای، مثل تلگرام.** پست، واکنش، حذف، ویرایش و رأی در گروه‌ها و کانال‌ها، و تغییر دسترسی‌ها مثل باز کردن «ارسال پیام»، حالا همان لحظه از راه دو سرور ایران گره به اعضا می‌رسد، بی آنکه برای هر عضو جدا فرستاده شود. سرور ایران همیشه اول است؛ صندوق گوگل و راه‌های دیگر فقط وقتی به کار می‌آیند که سرور ایران در دسترس نباشد. عضوی که مدتی دور بود، پست‌های جامانده را از سرور ایران می‌خواند. عضوهایی که هنوز نسخهٔ قدیمی دارند مثل قبل پیام می‌گیرند، کندتر.
- **گره: خبر پاسخ و نام شما در گروه، مثل تلگرام.** وقتی کسی در گروه یا گروه رسمی روی پیام شما پاسخ می‌دهد یا نام شما را با @ می‌نویسد، اعلان می‌آید، حتی اگر گروه بی‌صدا باشد، و تا آن را نبینید کنار گروه در فهرست گفت‌وگوها @ دیده می‌شود. پیش‌تر هیچ چیز نمی‌گفت که کسی جواب شما را داده است.
- **گره: سنجاق با خبرش.** وقتی پیامی در گروه، کانال، گفت‌وگوی تکی یا کانال و گروه رسمی سنجاق می‌شود، سطر «… سنجاق کرد» در گفت‌وگو می‌آید و اعلانش هم می‌رسد، مثل تلگرام؛ در گروه بی‌صدا هم، مگر «پیام‌های سنجاق‌شده» را در تنظیمات اعلان خاموش کنید. در کانال، سنجاق به نام خود کانال است. پیش‌تر سنجاق بی‌صدا بالای گفت‌وگو می‌نشست و کسی باخبر نمی‌شد.
- **گره: اینترنت و باتری کمتر.** وقتی سرور ایران گره در دسترس است، گره بیرون از برنامه هر ۵ دقیقه یک بار به صندوق گوگل سر می‌زند (پیش‌تر هر ۳۰ تا ۹۰ ثانیه)، پیامی را که صندوق گیرنده گم کرده بود دیگر پشت سر هم و تا یک هفته دوباره نمی‌فرستد، اتصال مستقیم گوشی‌به‌گوشی را آرام‌تر جست‌وجو می‌کند، و کانال و گروه رسمی را هر ۳ ساعت یک بار همگام می‌کند نه هر ۱۰ دقیقه. چیزی دیرتر نمی‌رسد، چون پیام‌ها از راه سرور ایران همان لحظه می‌رسند.
- **کانفیگ‌های ایران: سرورلس نسخهٔ ۵۹.** کانفیگ‌های ایران حالا نسخهٔ ۵۹ سرورلس ‎@patterniha را هم دارند: «oob»، «fragA» و «fragB»، هر کدام با DNS گوگل، کلادفلر یا AdGuard هم، روی هستهٔ Xray خود سازنده نسخهٔ 26.11.12 برای گوشی‌های ۶۴ و ۳۲ بیتی. کانفیگ‌های قبلی سر جایشان هستند.

### رفع‌شده
- **گره: «اجازهٔ ارسال پیام» در گروه ذخیره نمی‌شد.** مالک گروه در دسترسی‌ها «ارسال پیام» را برای اعضا باز می‌کرد و ذخیره می‌زد، ولی گروه بسته می‌ماند و اعضا «نوشتن پیام در این گروه مجاز نیست» می‌دیدند. حالا همان بار اول ذخیره می‌شود و اعضا همان لحظه می‌توانند بفرستند. همین ایراد گاهی پیوستن تازه‌واردها را هم بی‌صدا رد می‌کرد؛ آن هم درست شد.
- **گره: پیام‌ها روی بعضی گوشی‌ها بار نمی‌شد.** روی گوشی‌ای که منتظر پیوستن به چند گروه بود، گره پیوسته سرگرم همان کار می‌ماند و پیام‌ها و گفت‌وگوها دیر یا اصلاً باز نمی‌شدند. حالا این کار سبک شده و گفت‌وگوها زود باز می‌شوند.
- **گره: جست‌وجوی @نام گروه.** جست‌وجوی نام گروهی که در آن عضوید، مثل ‎@mlmwindows، گاهی صفحهٔ «افزودن کانال تلگرام» را باز می‌کرد، و گروه‌هایی که عضوشان بودید با @نامشان پیدا نمی‌شدند. حالا خود گروه پیدا و باز می‌شود.
- **فنیکس: خطا برطرف شد.** خطایی که فنیکس را از وصل شدن بازمی‌داشت برطرف شد.
- **پایداری: ده‌ها کرش و یخ‌زدگی گزارش‌شده درست شد.** از گزارش‌های خودکار کرش نسخه‌های ۱.۲.۴۷ و ۱.۲.۴۸: باز شدن گره پس از خطای هسته، جست‌وجو و نمایش عکس در گره، صفحهٔ پروفایل، ایمیل کلادفلری که نویسهٔ نامرئی داشت، سرویس‌های اسکن روی اندروید ۱۳ و پایین‌تر، مامی روی اندروید ۷، لنترن، نشان شمار پیام روی گوشی‌های سونی و نقشه در گفت‌وگو دیگر برنامه را نمی‌بندند. کارهای سنگین شروع برنامه، کاشی‌های خانه، ویجت‌ها، قطع OpenVPN، «باز شد» در MAE و آزمون گروهی کانفیگ‌ها از رشتهٔ اصلی بیرون رفت تا صفحه روی گوشی‌های ضعیف یخ نزند، و سقف حافظهٔ برنامه مثل خود تلگرام بالاتر رفت.

### کدام فایل را دانلود کنم؟
- **arm64-v8a:** بیشتر گوشی‌ها (۶۴ بیتی). اگر نمی‌دانید، همین را بگیرید.
- **armeabi-v7a:** گوشی‌های قدیمی‌تر ۳۲ بیتی.
- **universal:** روی همهٔ گوشی‌ها نصب می‌شود، ولی حجمش بیشتر است.
- به‌روزرسانی از داخل خود برنامه فایل درستِ گوشی شما را خودش برمی‌دارد.





### v1.2.48 — اتصال مستقیم بی سرور، مامی و آرگو؛ گفتار به متن و پیوستن فوری در گره (Stable)
- Tag: `v1.2.48`
- تاریخ انتشار: 2026-11-08T10:14:27Z
- صفحه رسمی: https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.48
- APKهای ARM64:
  - [mlmvpn-1.2.48-arm64-v8a-release.apk](https://github.com/mlmvpn/mlmvpn_android/releases/download/v1.2.48/mlmvpn-1.2.48-arm64-v8a-release.apk)

**یادداشت توسعه‌دهنده:**
## اتصال مستقیم بی سرور، مامی و آرگو؛ گفتار به متن و پیوستن فوری در گره

### افزوده‌شده
- **اتصال مستقیم: بی سرور و بی کانفیگ.** روش تازه‌ای در صفحهٔ اصلی: اولین بستهٔ هر اتصال طوری شکسته می‌شود که فیلتر نام سایت را نبیند (شکستن رکورد TLS، بُرش بسته، جابه‌جایی تکه‌ها و بایت خارج از باند)، و نام سایت‌ها با DNS رمزدار از چند سرویس پیدا می‌شوند و جواب‌هایی که به صفحهٔ فیلتر اشاره کنند رد می‌شوند. ترافیک مستقیم به خود سایت‌ها می‌رود، بی هیچ سروری در میان. برای هر سایت مسدود، روش‌ها خودکار امتحان می‌شوند و روشی که بازش کرد به خاطر سپرده می‌شود تا دفعهٔ بعد بی‌درنگ باز شود. سایتی که نشانی سرورش مسدود است، یا سرویسی که خودش ایران را نمی‌پذیرد، با این روش باز نمی‌شود و صفحه همین را می‌گوید. موتورش Shroudly است (متن‌باز). با کاشی بالای گوشی، ویجت‌ها، کلید قطع اضطراری، تونل جداگانهٔ برنامه‌ها، پشتیبان‌گیری و MLM Scout هماهنگ است.
- **مامی: شش روش در یک صفحه — خودکار، اختصاصی، سان، لیون، هوشمند و تایگر.** «خودکار»: گوشی به‌صورت ناشناس روی سرور مامی ثبت می‌شود — بی‌نام، بی‌شماره و بی‌حساب — و فهرست سرورها را رمزشده و امضاشده می‌گیرد؛ فهرستی که امضایش نخواند پذیرفته نمی‌شود. سرورها با یک درخواست واقعی سنجیده می‌شوند و سریع‌ترینی که واقعاً داده رد کند وصل می‌شود؛ اگر سروری وسط کار جواب ندهد، خودش به سرور بعدی می‌رود. مکان خروج را هم از میان همهٔ مکان‌های فهرست مامی می‌شود انتخاب کرد. «لیون»: پل‌هایی که دستگاه‌های دیگر آزموده‌اند، سنجیده و به ترتیب سابقهٔ موفقیت. «اختصاصی»: پلی که سرور مامی فقط برای همین گوشی می‌سازد. «سان»، «هوشمند» و «تایگر» سه راه دیگرند که روی گوشی همیشه تونل کامل‌اند. «وصل» فقط وقتی نشان داده می‌شود که یک درخواست واقعی از داخل اتصال رد شد.
- **آرگو VPN: پل‌ها، فالکن‌ها و سرورهای عمومی آرگو.** همان آرگوی ویندوز: پل‌ها و فالکن‌ها از کانال‌های تلگرام و گیت‌هاب و فهرست رسمی خود آرگو جمع می‌شوند و هر کدام واقعاً سنجیده می‌شود — دست‌دهی خود آرگو، یک درخواست واقعی از داخلش که کشور و آی‌پی خروج را معلوم می‌کند، و دانلود ۲۵۶ کیلوبایت تا سروری که وسط دانلود قطع می‌شود سالم شمرده نشود. یک ضربه سریع‌ترینِ سالم را وصل می‌کند. «آی‌پی تمیز» یک لبهٔ سالم کلادفلر پیدا می‌کند (TLS، دست‌دهی آرگو و دانلود واقعی، IPv4 و IPv6 جدا) که همهٔ پل‌ها و فالکن‌ها را با هم رفع فیلتر می‌کند. پل یا فالکن خودتان را بچسبانید، منبع تلگرام یا گیت‌هاب خودتان را اضافه کنید، یا با راهنمای «ساخت فالکن شخصی» فالکنی بسازید که فقط مال شماست. پل‌ها و فالکن‌هایی که در گفت‌وگوهای گره فرستاده می‌شوند هم مثل بقیهٔ کانفیگ‌ها شناخته می‌شوند: سنجیده می‌شوند و سالم‌هایشان با یک ضربه به فهرست آرگو می‌روند.
- **گره: تبدیل گفتار به متن در گفت‌وگو.** دکمهٔ میکروفون حالا حالت سومی دارد: یک بار لمس، ویدیو سلفی؛ یک بار دیگر، تبدیل گفتار به متن؛ و یک بار دیگر، دوباره پیام صوتی. دکمه را نگه دارید و حرف بزنید: کلمه‌ها همان‌طور که می‌گویید در کادر پیام دیده می‌شوند، با سرویس گفتار خود گوشی و بی هیچ پنجرهٔ گوگل روی صفحه. رها کنید، متن در کادر است تا بفرستید یا ویرایش کنید. مثل ضبط صدا، اگر هنگام نگه داشتن انگشت را به بالا بکشید قفل می‌شود و بی نگه داشتن حرف می‌زنید؛ برای پایان، توقف را بزنید.
- **گره: شمار بازدید پست‌های کانال.** هر پست در کانال‌های گره و کانال رسمی حالا نشان می‌دهد چند نفر دیده‌اندش؛ شمارش روی سرور ایران گره است، مثل تلگرام. سرور نه کانال را می‌فهمد، نه پست را و نه بیننده را، و هر نفر یک بار شمرده می‌شود. مدیر کانال می‌تواند با «نمایش تعداد بازدید» در صفحهٔ ویرایش کانال، شمار را از همه مخفی کند.
- **گره: اخطار در گروه و گروه رسمی.** مدیری که می‌تواند سکوت بدهد، حالا از روی پیام عضو به او اخطار می‌دهد، با دلیل اگر بخواهد. هر پیام یک اخطار، و اخطار چهارم عضو را برای همیشه بن می‌کند؛ در گروه فقط مالک این بن را برمی‌دارد و در گروه رسمی هیچ‌کس.
- **گره: گفت‌وگوی عمومی و خصوصی، مثل تلگرام.** کانال یا گروهی که نام کاربری با @ دارد عمومی است: هر کسی با نامش یا از فهرست عمومی بی انتظار تأیید عضو می‌شود (مگر مالک «تأیید اعضای جدید» را روشن کند)، و پیش از پیوستن آخرین پست‌هایش را می‌بیند. گفت‌وگوی بی‌نام خصوصی است و فقط با پیوند دعوتش. نوع هر کانال و گروه، عمومی یا خصوصی، در صفحهٔ ویرایش آن هم انتخاب می‌شود: عمومی نام @ می‌گیرد و خصوصی آن را رها می‌کند.
- **گره: ذخیرهٔ گیف.** «ذخیرهٔ گیف» کار می‌کند: گیف‌هایی که ذخیره می‌کنید در فهرست گیف همان گوشی می‌مانند و می‌توانید دوباره از همان‌جا بفرستید.
- **کانفیگ‌های ایران: سرورلس نسخهٔ ۵۸.** کانفیگ‌های ایران حالا نسخهٔ ۵۸ سرورلس ‎@patterniha را هم دارند: «oob» برای خط‌های همراه اول و «fragA» و «fragB» برای ایرانسل، هر کدام با DNS گوگل، کلادفلر یا AdGuard هم. این کانفیگ‌ها از نسخهٔ ۵۷ فقط با هستهٔ Xray خود سازنده اجرا می‌شوند؛ پس برنامه حالا آن هسته را برای گوشی‌های ۶۴ و ۳۲ بیتی همراه دارد و برای هر کانفیگ خودش هستهٔ درست را انتخاب می‌کند. بقیهٔ کانفیگ‌ها مثل قبل روی Xray رسمی می‌مانند. استور هم به‌روزرسانی کانفیگ‌ها و هسته را دنبال می‌کند.

### رفع‌شده
- **کاشی بالای گوشی با همهٔ روش‌ها هماهنگ شد.** کاشی MLMVPN در منوی کشویی گوشی، URnetwork، وارپ، لنترن و گف را روشن نشان نمی‌داد و زدنش آن‌ها را قطع نمی‌کرد. حالا هر روشی که وصل یا در حال اتصال است روشن نشان داده می‌شود و نام روش زیرش می‌آید، و زدن کاشی همه را قطع می‌کند؛ از جمله MAE، گیت‌هاب تانل، SNI و پروتون که خودشان دوباره وصل می‌شدند. اتصالی که هنوز در حال برقراری است هم با زدن کاشی لغو می‌شود، و کاشی تا منو باز است با هر تغییر به‌روز می‌شود. وقتی «کلید قطع اضطراری» پس از افتادن تونل اینترنت را بسته نگه می‌داشت، «قطع» بازش نمی‌کرد؛ حالا باز می‌کند. و روشن کردن یک روش وقتی URnetwork یا روش دیگری هنوز در حال اتصال بود نادیده گرفته می‌شد؛ حالا اول قبلی بسته می‌شود.
- **فنیکس: بررسی مرورگر موزیلا دیگر پشت سر هم باز نمی‌شود.** موزیلا روی خط‌های ایران پیش از ورود و اتصال یک بررسی مرورگر می‌خواهد. حالا برنامه اول خودش این بررسی را می‌گذراند و صفحه‌اش فقط وقتی باز می‌شود که لازم باشد، با یک راهنمای کوتاه. پس از گذراندن بررسی، کاری که نیمه مانده بود (اتصال یا افزودن حساب) خودش ادامه پیدا می‌کند و ورود دوباره لازم نیست. اگر موزیلا درست پس از بررسی هم نپذیرد، صفحه دیگر با هر اتصال دوباره باز نمی‌شود و برنامه می‌گوید چند ساعت بعد امتحان کنید. حساب هم فقط وقتی از برنامه خارج می‌شود که موزیلا بگوید ورودش دیگر معتبر نیست، نه با هر خطای گذرا.
- **گره: پیوستن به گروه و کانال عمومی، فوری و بی نیاز به مالک.** در گروه‌های عمومی بزرگ (مثل گروهی با ۳۵۰ عضو) کسی نمی‌توانست بپیوندد، حتی وقتی گوشی مالک روشن بود. حالا عضویت در گفت‌وگوهای عمومی روی سرور گره هم ثبت می‌شود و پیوستن همان لحظه انجام می‌شود، بی آنکه مالک یا مدیری آنلاین باشد. پست‌هایی که پیش از پیوستن در پیش‌نمایش دیدید، پس از پیوستن هم در گفت‌وگو می‌مانند. «پیوستن» در گفت‌وگوی باز دیگر «درخواست» نمی‌گوید و گفت‌وگو همان دم باز می‌شود، و گفت‌وگویی که اعضای تازه را تأیید می‌کند پیش از تأیید پستی نشان نمی‌دهد. برای گفت‌وگوی قدیمی کافی است مالک یا یکی از مدیرانش یک بار برنامه را با این نسخه باز کند؛ عضوهایی که هنوز نسخهٔ قدیمی دارند تا به‌روزرسانی پیام تازه‌واردها را نمی‌بینند.
- **کانفیگ‌های ایران: تست و اتصال با ضربهٔ دوم متوقف می‌شوند.** تستی که شروع می‌شد دیگر متوقف نمی‌شد؛ حالا ضربهٔ دوباره روی دکمهٔ تست آن را متوقف می‌کند و نتیجهٔ کانفیگ‌هایی که تا آن لحظه سنجیده شده‌اند می‌ماند. کانفیگی هم که در حال اتصال است با ضربهٔ دوباره لغو می‌شود؛ پیش‌تر ضربه فقط اتصال را از نو شروع می‌کرد.
- **گره: چند عکس یا ویدیو که با هم فرستاده می‌شد به‌هم می‌ریخت.** دو سه عکس که با هم در کانال فرستاده می‌شد، تک‌تک و هر کدام همین که آپلودش تمام می‌شد می‌رفت، و جدا و نامرتب می‌رسید. حالا مثل تلگرام اول همهٔ عکس‌ها و ویدیوها آپلود می‌شوند و بعد همه با هم یک آلبوم می‌روند، در پی‌وی، گروه و کانال؛ هر کدام آپلود خودش را نشان می‌دهد و هر کدام را لغو کنید کنار می‌رود.
- **گره: عکس پروفایل کانال‌ها با هر باز شدن برنامه خالی بود.** عکس کانال تلگرامی‌ای که در گره افزوده شده، با هر بار خواندن صفحه‌اش زیر نامی تازه دوباره دانلود می‌شد و با باز شدن برنامه کانال‌ها بی عکس بودند. حالا عکس روی گوشی می‌ماند، روزی یک بار سنجیده و فقط اگر واقعاً عوض شده باشد دوباره دانلود می‌شود، و کانال‌ها همان لحظهٔ باز شدن برنامه عکس دارند.
- **گره: پیام اول صف، و بی سقف عضو.** پیام‌ها در صف ارسال همیشه پیش از فایل‌ها می‌روند تا انبوه تکه‌های فایل دیگر پیام‌های کوتاه را نگه ندارد، و تکهٔ فایلی که رلهٔ ما نمی‌پذیرد دیگر پیام‌ها به آن را متوقف نمی‌کند. گروه و کانال دیگر در ۲۰۰ عضو نمی‌ایستند.
- **گره: رلهٔ دوم ایران به‌عنوان پشتیبان.** گره حالا روی رلهٔ دومی در ایران هم می‌نویسد و از هر دو می‌خواند، تا وقتی یکی مشکل دارد پیام‌ها و پست‌های رسمی همچنان برسند. رله‌های ما دیگر تکهٔ فایل نسخه‌های قدیمی را که پرشان کرده بود نمی‌پذیرند؛ فایل‌ها از راه هاست دانلود می‌روند.
- **گره: بسته شدن ناگهانی هنگام بارگذاری ایموجی‌ها.** روی بعضی گوشی‌ها بخش گفت‌وگو هنگام بارگذاری ایموجی‌ها ناگهان بسته می‌شد. حالا اگر بستهٔ ایموجی از درون برنامه باز نشود، یک بار در حافظهٔ برنامه کپی و از همان‌جا خوانده می‌شود، و این خطا دیگر برنامه را نمی‌بندد.

### کدام فایل را دانلود کنم؟
- **arm64-v8a:** بیشتر گوشی‌ها (۶۴ بیتی). اگر نمی‌دانید، همین را بگیرید.
- **armeabi-v7a:** گوشی‌های قدیمی‌تر ۳۲ بیتی.
- **universal:** روی همهٔ گوشی‌ها نصب می‌شود، ولی حجمش بیشتر است.
- به‌روزرسانی از داخل خود برنامه فایل درستِ گوشی شما را خودش برمی‌دارد.


### v1.2.47 — پیام دوطرفه، آپلود واقعی و مصرف اینترنت کمتر در گره (Stable)
- Tag: `v1.2.47`
- تاریخ انتشار: 2026-11-03T17:37:47Z
- صفحه رسمی: https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.47
- APKهای ARM64:
  - [mlmvpn-1.2.47-arm64-v8a-release.apk](https://github.com/mlmvpn/mlmvpn_android/releases/download/v1.2.47/mlmvpn-1.2.47-arm64-v8a-release.apk)

**یادداشت توسعه‌دهنده:**
## پیام دوطرفه، آپلود واقعی و مصرف اینترنت کمتر در گره

### رفع‌شده
- **گره: پیام خصوصی‌ای که برای همیشه روی ساعت می‌ماند.** پیام به مخاطبی که کارتش هیچ رله‌ای نداشت (کارتی از نسخه‌های قدیمی، یا کارتی که وقتی گوشی‌اش به رلهٔ ایران گره نمی‌رسید ساخته شده بود) راهی برای رفتن نداشت: برای همیشه روی ساعت می‌ماند و طرف مقابل هرگز از شما خبردار نمی‌شد. حالا هر پیام از رلهٔ گره هم می‌رود، که همهٔ گوشی‌ها از آن می‌خوانند، و جواب هم برمی‌گردد. کارت خود شما هم حالا همیشه این رله را دارد.
- **گره: مصرف اینترنت خیلی کمتر.** هر بار که گره دوباره وصل می‌شد (روی هر گوشی حدود هر ۱۰ دقیقه)، پست‌های رسمی و پیام‌های ۳ ساعت گذشته را که از قبل داشت از نو دانلود می‌کرد؛ این ۸۱٪ همهٔ چیزی بود که رلهٔ گره می‌فرستاد. حالا فقط آنچه از آخرین اتصال آمده گرفته می‌شود.
- **گره: پیام خصوصی پس از رسیدن از سرور پاک می‌شود.** پیام خصوصی‌ای که از راه رلهٔ گره می‌رود، حالا همین که به گوشی گیرنده رسید از سرور پاک می‌شود، و فقط همان گوشی می‌تواند پاکش کند. تا وقتی گیرنده آفلاین است، پیام تا ۱۴ روز برایش می‌ماند (پیش‌تر ۲ روز، و وقتی دیسک رله پر می‌شد گاهی فقط چند ساعت). پیام‌های گروه ۷ روز می‌مانند. تکه‌های فایل دیگر روی رلهٔ گره انباشته نمی‌شوند.
- **گره: پیام فایل فقط وقتی می‌رود که فایل دانلودشدنی باشد.** فرستادن عکس، ویدیو یا فایل در چند ثانیه «تمام» نشان داده می‌شد، در حالی که آپلود پشت صحنه ادامه داشت و طرف مقابل فایلی می‌گرفت که هنوز باز نمی‌شد. حالا نوار، آپلود واقعی را نشان می‌دهد، پیام فقط وقتی می‌رود که هاست دانلود گره فایل را داشته باشد، و ضربه روی × آپلود را همان لحظه قطع می‌کند و چیزی فرستاده نمی‌شود. اگر سرور فایل را نپذیرد یا فایل به آن نرسد، پیام «نرفته» علامت می‌خورد تا دوباره بفرستید. روی اینترنتی که آپلود به سرور گره را می‌بندد، فایل پس از چند ثانیه از راه قبلی می‌رود.
- **گره: «نسخهٔ قدیمی» کنار همهٔ کسانی که نسخهٔ قدیمی دارند.** برچسب «نسخهٔ قدیمی» کنار نام خیلی از کسانی که نسخهٔ قدیمی داشتند دیده نمی‌شد و گوشی‌ها با هم فرق داشتند: هر گوشی فقط با نسخهٔ خودش یا با بررسی به‌روزرسانی می‌سنجید که اغلب به گیت‌هاب نمی‌رسد، و نویسنده‌های گروه رسمی اغلب اصلاً سنجیده نمی‌شدند. حالا هر گوشی تازه‌ترین نسخه را از کسانی که می‌نویسند هم یاد می‌گیرد، پس برچسب همه‌جا یکی است، در گفت‌وگوی خصوصی، گروه و گروه رسمی، و وقتی آن کاربر به‌روز کند برداشته می‌شود.
- **گره: گزارش عیب‌یابی دقیق‌تر.** گزارشی که هر گوشی برای پیدا کردن مشکل‌ها روی سرور گره می‌گذارد، حالا بی هیچ محتوایی از پیام‌ها این را هم می‌شمارد: چند پیامِ رسیده باز نشد، پیام‌ها چرا منتظرند و هر آپلود فایل چه شد؛ تا مشکلی مثل پیام یک‌طرفه را بشود دنبال کرد.

### کدام فایل را دانلود کنم؟
- **arm64-v8a:** بیشتر گوشی‌ها (۶۴ بیتی). اگر نمی‌دانید، همین را بگیرید.
- **armeabi-v7a:** گوشی‌های قدیمی‌تر ۳۲ بیتی.
- **universal:** روی همهٔ گوشی‌ها نصب می‌شود، ولی حجمش بیشتر است.
- به‌روزرسانی از داخل خود برنامه فایل درستِ گوشی شما را خودش برمی‌دارد.


### v1.2.46 — هاست دانلود برای همهٔ فایل‌ها و عکس‌ها، تا ۵۰ مگابایت (Stable)
- Tag: `v1.2.46`
- تاریخ انتشار: 2026-11-02T03:36:33Z
- صفحه رسمی: https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.46
- APKهای ARM64:
  - [mlmvpn-1.2.46-arm64-v8a-release.apk](https://github.com/mlmvpn/mlmvpn_android/releases/download/v1.2.46/mlmvpn-1.2.46-arm64-v8a-release.apk)

**یادداشت توسعه‌دهنده:**
## هاست دانلود برای همهٔ فایل‌ها و عکس‌ها، تا ۵۰ مگابایت

### افزوده‌شده
- **گره: هاست دانلود برای همهٔ فایل‌ها و عکس‌ها، تا ۵۰ مگابایت.** هر عکس، ویدیو، پیام صوتی و فایلی که در پی‌وی، گروه، کانال و گفت‌وگوهای رسمی می‌فرستید، و عکس پروفایل و عکس گروه و کانال، یک بار روی هاست دانلود گره می‌رود و همه از همان‌جا دانلود می‌کنند، حتی وقتی فرستنده آفلاین است. دانلودِ قطع‌شده از همان‌جا ادامه پیدا می‌کند. همه‌چیز پیش از رفتن روی گوشی رمز می‌شود: هاست فقط دادهٔ رمزشده می‌بیند و گوشی گیرنده هر تکه را با کلید فایل می‌سنجد، پس کسی نمی‌تواند فایل را عوض کند. سقف هر فایل از ۲۰ به ۵۰ مگابایت رسید. فایل‌های «پیام‌های ذخیره‌شده» از گوشی بیرون نمی‌روند.
- **گره: گزارش عیب‌یابی به سرور گره.** تا مشکل هر کاربر را بشود دید و رفع کرد (پیامی که نمی‌رسد، پستی که در گروه رسمی رد می‌شود)، گره یک دقیقه پس از باز شدن، هر شش ساعت و پس از هر مشکل گزارش کوتاهی برای سرور گره می‌فرستد: کارت شما، نسخهٔ برنامه، وضعیت رله‌ها، پیام‌هایی که منتظر مانده‌اند و چرا، و وضعیت شما در گفت‌وگوهای رسمی. متن پیام‌ها، فایل‌ها و کلید مخاطبان هرگز در آن نیست، گزارش با کلید خود شما امضا می‌شود.
- **گره: نام کاربری با @ به‌جای کارت.** هر کاربر، کانال و گروه حالا می‌تواند یک نام کاربری اختصاصی داشته باشد، مثل ‎@mlmvpn. نام خودتان را از «تنظیمات › نام کاربری» بگذارید؛ سرور گره همان لحظه می‌گوید آزاد است یا گرفته شده. دیگران به‌جای کارت، با نوشتن ‎@نام شما در جستجو یا در «مخاطب تازه» پیدایتان می‌کنند، و با اولین پیام مخاطب هم می‌شوید. مالک کانال یا گروه هم از صفحهٔ ویرایش آن «نام کاربری» می‌گذارد؛ با ‎@نامش در جستجو پیدا می‌شود، و ‎@نامش در یک پیام، برای کسی که عضو نیست، صفحهٔ پیوستن را باز می‌کند. پیوند هر نام «gereh/نام» است، نه t.me، و در پیام لمس‌شدنی است؛ پیوند t.me در گره حالا در اپ تلگرام یا مرورگر باز می‌شود.

### رفع‌شده
- **گره: پیامی که یک تیک می‌ماند و هرگز نمی‌رسید.** پیام تکی‌ای که از راه رله یا رلهٔ گوگل می‌رفت، همین که رله آن را می‌گرفت «فرستاده» حساب می‌شد؛ اگر رله بعد آن را گم می‌کرد، پیام هرگز نمی‌رسید. حالا تا گوشی مقابل رسیدنش را تأیید نکند، پس از ۱، ۲، ۴، ۸، ۱۶ و ۳۲ ساعت دوباره فرستاده می‌شود.
- **گره: کندی شدید روی گوشی مدیر گفت‌وگوهای رسمی.** روی گوشی‌ای با صف ارسال بزرگ (مثل مدیر کانال و گروه رسمی)، هر بار که مخاطبی دیده می‌شد کل صف خوانده می‌شد و گره چند ثانیه هنگ می‌کرد. حالا این کار در چند میلی‌ثانیه انجام می‌شود.
- **گره: دانلودی که گیر می‌کرد.** دانلودی که ۳۰ ثانیه چیزی نیاورد رها می‌شود تا دوباره بزنید (پیش‌تر ۶۰ ثانیه)، و آیکون دانلود کنار منو وقتی فهرستش خالی است دیگر روشن نمی‌ماند.
- **گره: رلهٔ ایران ده ساعت از کار افتاده بود.** پاک‌سازی خودکار رلهٔ ایران دیسکش را پر می‌کرد و ده ساعت هیچ پیام و عکسی از آن رد نشد. حالا پاک‌سازی هرگز دیسک را پر نمی‌کند، و فایل‌ها دیگر روی رله نمی‌مانند و فقط از آن به هاست دانلود می‌روند.
- **کانفیگ‌های کلادفلر که پینگ می‌دادند ولی وصل نمی‌شدند.** روی بعضی خط‌ها (مثل وای‌فای همراه اول) کلادفلر روی IPv4 پینگ و دانلود را رد می‌کند ولی آپلود را پس از چند بسته قطع می‌کند. حالا روشی که روی IPv6 کلادفلر جواب داده با همان IPv6 وصل می‌شود، اتصالی که داده نبرد روی IPv6 دوباره امتحان می‌شود، بررسی وصل شدن یک آپلود واقعی است، و اتصال ناموفق تونل مرده باقی نمی‌گذارد. «آرنا» هم فقط آی‌پی تمیزی را برمی‌دارد که آپلود را رد می‌کند.
- **گره: پیام در گروه رسمی «!» می‌گرفت و دلیلش گفته نمی‌شد.** هر پستی که گروه رسمی نمی‌پذیرفت «در این کانال فقط مدیران می‌نویسند» می‌گفت. حالا دلیل واقعی گفته می‌شود: لینک، ارسال آهسته، گوشی مسدود، یا مسدود و ساکت بودن. نام فایل‌ها (مثل config.json یا wg.conf) و کلمه‌ای که پس از نقطه بی‌فاصله آمده هم دیگر لینک حساب نمی‌شود و پست را رد نمی‌کند.

### کدام فایل را دانلود کنم؟
- **arm64-v8a:** بیشتر گوشی‌ها (۶۴ بیتی). اگر نمی‌دانید، همین را بگیرید.
- **armeabi-v7a:** گوشی‌های قدیمی‌تر ۳۲ بیتی.
- **universal:** روی همهٔ گوشی‌ها نصب می‌شود، ولی حجمش بیشتر است.
- به‌روزرسانی از داخل خود برنامه فایل درستِ گوشی شما را خودش برمی‌دارد.



### v1.2.45 — رفع هنگ و بسته شدن گره، و رلهٔ ایران دوباره سر پا (Stable)
- Tag: `v1.2.45`
- تاریخ انتشار: 2026-10-31T21:09:53Z
- صفحه رسمی: https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.45
- APKهای ARM64:
  - [mlmvpn-1.2.45-arm64-v8a-release.apk](https://github.com/mlmvpn/mlmvpn_android/releases/download/v1.2.45/mlmvpn-1.2.45-arm64-v8a-release.apk)

**یادداشت توسعه‌دهنده:**
## رفع هنگ و بسته شدن گره، و رلهٔ ایران دوباره سر پا

### افزوده‌شده
- **گره: جستجو در گره و در تلگرام.** در جستجوی فهرست گفت‌وگوها، زیر «جستجو در گره» کانال‌ها و گروه‌های گره هم پیدا می‌شوند: اول آنچه به کلمه‌های شما نزدیک‌تر است، بعد پرمخاطب‌تر و قدیمی‌تر. با زدن روی یکی عضو می‌شوید (کانال همان دم، گروه با تأیید مدیرانش). صاحب کانال یا گروه می‌تواند در صفحهٔ ویرایش «نمایش در جستجو» را خاموش کند. زیر «جستجو در تلگرام» کانال‌های عمومی تلگرام از راه اسکریپت تلگرام خودتان می‌آیند و با یک زدن به گره افزوده می‌شوند. اگر اسکریپت را پیش از این نسخه ساخته‌اید، یک بار کد تازه‌اش را در گوگل بگذارید.
- **گره: کانال‌های تلگرام در گره.** از منوی «پیام تازه» یک کانال عمومی تلگرام را با نامش بیفزایید. گره پست‌ها، عکس‌ها و ویدیوهایش را از راه اسکریپت گوگل خودتان می‌خواند و فقط روی گوشی شما نگه می‌دارد؛ گوشی هرگز به تلگرام وصل نمی‌شود. «به‌روزرسانی» پست‌های تازه را می‌آورد، با زمان‌سنج دلخواه. خودتان انتخاب می‌کنید فایل‌ها هم بیایند یا نه، تا چه حجمی، و همین حالا یا بعداً؛ گره حجم و شمار درخواست‌ها را هم می‌گوید.
- **گره: کاشی‌ها و تنظیمات برنامه در گفت‌وگو.** از منوی پیوست («MLMVPN» و «تنظیمات») یک کاشی یا یک گزینهٔ تنظیمات برنامه را بفرستید؛ در گفت‌وگو کارتی شیک با دکمهٔ «باز کردن در MLMVPN» می‌آید و گیرنده با یک زدن همان بخش برنامه را باز می‌کند. کارت روی خود هر گوشی کشیده می‌شود، پس هیچ دانلودی نمی‌خواهد، حتی وقتی هدایت شود.
- **گره: زبانهٔ «کانفیگ‌ها» در اطلاعات گروه و کانال.** همهٔ کانفیگ‌های یک گفت‌وگو (لینک‌ها، NPV، OpenVPN، WireGuard، Amnezia و فهرست‌ها) در زبانه‌ای کنار «رسانه» و «پیوندها». زبانه‌های رسانه، فایل، صدا، موسیقی، پیوند و گیف هم که خالی بودند، حالا پر می‌شوند.
- **گره: «سکوت» روی پیام عضو، و سکوت موقت.** در گروه، با زدن روی پیام یک عضو «سکوت» می‌آید: از ۳۰ دقیقه تا یک هفته، یا برای همیشه، و برای کسی که ساکت است «برداشتن سکوت». همهٔ مدیران گروه رسمی هم می‌توانند. عضو ساکت‌شده می‌بیند چقدر مانده.
- **گره: ارسال آهسته در گروه رسمی.** مدیران گروه رسمی می‌توانند بگذارند هر عضو فقط هر چند ثانیه یک پیام بفرستد.
- **گره: منوی کاشی گره.** روی کاشی گره انتخاب کنید گره در پس‌زمینه بماند یا فقط وقتی باز است کار کند، و همهٔ گره را بی‌صدا کنید.
- **گره روی گوشی‌های ۳۲ بیتی.** گره حالا روی گوشی‌های قدیمی‌تر با پردازندهٔ ۳۲ بیتی (armeabi-v7a) هم باز می‌شود؛ پیش‌تر می‌گفت گوشی ۶۴ بیتی لازم است.
- **گره: نظرسنجی در گروه و کانال.** نظرسنجی خود تلگرام: پرسش با تا ۱۰ گزینه، تک‌گزینه یا چندگزینه، یا آزمونک. مثل تلگرام ناشناس است، مگر سازنده خاموشش کند. رأی را می‌شود پس گرفت یا عوض کرد، و خوانندهٔ کانال هم رأی می‌دهد.
- **گره: فایل‌های کانال‌های تلگرام.** زیر پستِ کانال تلگرام که فایل دارد (npvs، ovpn، conf و …) دکمهٔ «دریافت» می‌آید؛ با یک زدن فایل می‌رسد و پست همان‌جا خودِ فایل می‌شود. روزی ۲۰ فایل برای هر گوشی.
- **گره: «سنجش» و «انتقال» زیر کانفیگ‌های کانال تلگرام.** کانفیگی که در پست کانال تلگرام است، مثل کانفیگ‌های گفت‌وگوها، همان‌جا سنجیده یا به بخش درستِ برنامه منتقل می‌شود.
- **گره: فایل‌های NPV در گفت‌وگو.** زیر فایل npvs و npvt دکمهٔ «باز کردن در NPV Tunnel» و «انتقال» است، و در صفحهٔ NPV فایل‌هایی که گرفته‌اید با نام درستشان بالای صفحه می‌آیند.
- **گره: انتخاب رله.** آیکون دو پیکان بالای گره فهرست رله‌ها را با وضعیت هر کدام نشان می‌دهد: «خودکار»، «سنجش همهٔ رله‌ها»، یا یک رله به انتخاب خودتان. رلهٔ انتخابی همیشه باز و اول است و بقیه پشتیبانش می‌مانند تا گفت‌وگو نایستد.
- **گره: ارسال آهسته در گروه‌های عادی.** مدیری که اجازهٔ مسدود کردن دارد، در «دسترسی‌ها»ی گروه می‌گذارد هر عضو فقط هر چند ثانیه یک پیام بفرستد؛ عضو زمان باقی‌مانده را می‌بیند.
- **گره: فهرست کاربران حذف‌شده در گروه.** در «دسترسی‌ها»ی گروه، «کاربران حذف‌شده» همهٔ بن‌شده‌ها را نشان می‌دهد؛ با زدن روی هر نفر بنش برداشته می‌شود.
- **گره: برچسب «نسخهٔ قدیمی».** کنار کسی که برنامه‌اش را به‌روز نکرده، در پیام‌ها، زیر نامش و در فهرست اعضا «نسخهٔ قدیمی» می‌آید، و اگر برنامهٔ خودتان قدیمی باشد به خودتان هم گفته می‌شود.
- **گره: پاک کردن داده، حذف حساب یا برداشتن گره.** در منوی کاشی گره: پاک کردن پیام‌ها و فایل‌های گره، حذف حساب، یا برداشتن کامل گره از برنامه؛ «بازگرداندن گره» در تنظیمات برنامه است.
- **گره: کانال و گروه رسمی مشترک با دکتر نت.** کاربران MLMVPN و دکتر نت حالا یک کانال و یک گروه رسمی دارند، و هر برنامه آن را با نام خودش نشان می‌دهد.
- **حمایت از گره.** قلب کنار منوی بالای گره: اگر گره به کارتان آمده، با یک حمایت کوچک به ادامهٔ ساختش، زیرساخت و قابلیت‌های تازه کمک کنید.

### رفع‌شده
- **گره: پیوستن با لینک می‌گفت «درخواست فرستاده شد» در حالی که نرسیده بود.** درخواست پیوستن به گروه یا کانالی که مدیرانش اعضا را تأیید می‌کنند، تا وقتی گوشیِ سازندهٔ لینک در دسترس باشد در صف می‌ماند. گره حالا به‌جای «فرستاده شد» می‌گوید در صف است، و همین که آن گوشی آنلاین شود، در چند ثانیه به مدیران می‌رسد.
- **گره: مشترکان کانال را فقط مدیرانش می‌بینند.** مثل تلگرام، فقط مدیران کانال می‌بینند چه کسانی عضو شده‌اند؛ بقیه فقط شمار را می‌بینند.
- **گره: گفت‌وگوهای رسمی صفحه‌ها را هنگ می‌کرد و چت‌ها بار نمی‌شد.** برای هر نامی که روی صفحه بود، گره کانال یا گروه رسمی را از همهٔ پست‌ها و واکنش‌ها از نو می‌ساخت و امضای هر کدام را دوباره می‌سنجید. حالا یک بار ساخته می‌شود و تا چیزی عوض نشده همان می‌ماند.
- **گره در خیلی از گوشی‌ها هنگ می‌کرد و بسته می‌شد.** صفحه‌های گره منتظر همگام‌سازی گفت‌وگوهای رسمی می‌ماندند و سرویس پس‌زمینهٔ گره به‌موقع بالا نمی‌آمد، پس اندروید آن را می‌بست. همگام‌سازی حالا سبک است و روی رشتهٔ اصلی نیست: وقتی گفت‌وگوی رسمی باز است هر ۴۵ ثانیه و وقتی برنامه جلوست هر ۱۰ دقیقه؛ پست‌ها همچنان از مخاطب‌ها همان دم می‌رسند.
- **گره تمام روز باتری می‌خورد.** وقتی گره روی صفحه نیست، دیگر بلوتوث را مدام جست‌وجو نمی‌کند (گوشی‌های دیگر هنوز گوشی شما را پیدا می‌کنند) و وای‌فای را برای هر پیام همگانی شبکه بیدار نگه نمی‌دارد. گروه رسمی هم بی‌صداست تا خودتان صدایش را باز کنید (کانال رسمی همچنان اعلان دارد). با رفع سیلِ بالا، گره در پس‌زمینه تقریباً آرام می‌ماند. ارتباط بلوتوثی هم حالا به‌طور پیش‌فرض خاموش است و کلیدش در پروفایل شماست.
- **گره: پیام دیگران فقط پس از فرستادن پیامی از خودتان می‌رسید.** اتصالی که شبکه بی‌صدا قطع کرده بود زنده به نظر می‌آمد و تا خودتان چیزی نمی‌فرستادید پیامی نمی‌رسید. حالا حداکثر در حدود یک دقیقه فهمیده و دوباره باز می‌شود و پیام‌های مانده همان دم می‌رسند.
- **گره: لینک وب و @کانال از اعضا در گروه رسمی ممنوع شد.** گروه پر از تبلیغ شده بود: پست عضوی که لینک وب، لینک t.me، دامنه یا @کانال دارد حالا رد می‌شود و جایی نشان داده نمی‌شود. لینک کانفیگ (vless، ss، trojan و بقیه) آزاد است و مدیران هر چیزی می‌توانند بفرستند.
- **گره: کانال و گروه رسمی بی‌عکس دیده می‌شد.** عکسشان حداکثر دو هفته روی رله می‌ماند؛ حالا برای همیشه می‌ماند و برای همه بار می‌شود.
- **گره: پیام و دانلود از راه رلهٔ ایران از کار افتاده بود.** هر پست رسمی برای همهٔ مخاطب‌های یک روز گذشته جدا فرستاده می‌شد و رله پر شد. حالا فقط به مخاطب‌هایی می‌رود که در ۱۰ دقیقهٔ گذشته در دسترس بوده‌اند و بقیه از رونوشت رسمی می‌خوانند. خود رله هم حالا سقف ذخیره دارد و قدیمی‌ترین داده را خودش پاک می‌کند.
- **گره: هر فایل حداکثر ۲۰ مگابایت.** در گفت‌وگوی تکی، گروه، کانال و گفت‌وگوهای رسمی؛ گره پیش از فرستادن می‌گوید.
- **گره: «سنجاق» در منوی پیام.** صاحب و مدیرانی که اجازهٔ سنجاق دارند، در گروه، کانال و گفت‌وگوهای رسمی، و هر دو طرف گفت‌وگوی تکی، حالا با زدن روی پیام «سنجاق» را می‌بینند؛ این گزینه پنهان مانده بود.
- **گره: «پیام‌های ذخیره‌شده».** پیامی که برای خودتان می‌فرستید حالا روی همین گوشی نگه داشته می‌شود و دیگر «!» نمی‌گیرد، و متن‌های این گفت‌وگو درست شد.
- **گره: زبانه‌های بی‌کار جستجو برداشته شد.** «برنامه‌ها» و «پست‌ها» از جستجو رفت، چون گره برنامهٔ کوچک ندارد و هیچ گوشی نمی‌تواند پست‌های گفت‌وگویی را که در آن نیست بگردد.
- **گره: وقتی رلهٔ ایران مشکل داشت، گفت‌وگوها می‌ایستاد.** یک پاسخ «شلوغم» از رلهٔ ایران گوشی را تا بستن برنامه از آن دور می‌کرد، کارت هر کس به مخاطبانش فقط رلهٔ ایران را می‌گفت، و یک خاموش‌وروشن چندثانیه‌ای رله، ده دقیقه قطعی می‌ساخت. حالا رلهٔ ایران چند ثانیه بعد دوباره امتحان می‌شود، پیام‌ها از رله‌های دیگری که گوشی می‌خواند و از رلهٔ گوگل هم می‌روند، و فایل‌ها دادهٔ چندبرابر نمی‌خورند.
- **گره: پست‌های کانال و گروه رسمی بی‌درنگ.** هر پست رسمی یک بار روی رلهٔ ایران گذاشته می‌شود و هر گوشی همان دم می‌گیردش، حتی گوشی‌ای که هیچ مخاطبی ندارد.
- **گره: هدایت پیام در همهٔ جهت‌ها.** هدایت (فوروارد) از کانال به کانال، از کانال تلگرام به پی‌وی و گروه، از گروه به پی‌وی و کانال و از پی‌وی به پی‌وی همیشه «!» می‌گرفت؛ حالا پیام از همین گوشی دوباره فرستاده می‌شود، بی «هدایت‌شده از».
- **گره: لینک پروکسی تلگرام در خود تلگرام باز می‌شود.** زدن روی لینک پروکسی تلگرام (MTProto یا SOCKS) در گره آن را در برنامهٔ تلگرام باز می‌کند و زیرش دکمهٔ «باز کردن در تلگرام» هست؛ پیش‌تر گره پروکسی را روی خودش روشن می‌کرد.
- **گره: عکس‌ها زودتر، و همیشه سر جایشان.** تا عکس کامل برسد، پیش‌نمایش محوش نشان داده می‌شود (گروه، کانال، کاربر و صفحهٔ اطلاعات)، و عکس گروه‌ها و کانال‌های عادی هم روی رلهٔ ایران می‌ماند و برای همه زود بار می‌شود.
- **گره: پست دیررسیده سر جای زمانی‌اش.** پست رسمی که دیر می‌رسید زیر پیام‌های تازه‌تر می‌نشست؛ حالا سر جای زمان خودش است.
- **گره: یک حساب برای هر گوشی در گروه رسمی.** تبلیغ‌کننده‌ای که بیرون می‌شد با حساب تازه از همان گوشی برمی‌گشت؛ حالا بن روی خود گوشی است. پست نسخه‌های قدیمی در گروه رسمی دیده نمی‌شود: برای نوشتن در آن به‌روز کنید.
- **گره: رفع کرش‌های گزارش‌شده.** کرش‌های ۱.۲.۴۳ و ۱.۲.۴۴ رفع شد: بیش از همه سرویس گره (حدود ۶۵۰ گزارش)، و پخش پیام صوتی، فهرست دانلودها و باز شدن برنامه پیش از نخستین باز کردن قفل گوشی پس از روشن شدن. دکمهٔ «مکان» تا ساخته شدنش از منوی پیوست برداشته شد.
- **فنیکس روی خط ایران وصل نمی‌شد.** موزیلا روی خط ایران اول «بررسی مرورگر» می‌خواهد؛ این صفحه حالا برای همان سروری باز می‌شود که آن را خواسته، با کوکی جدای هر سایت.
- **آمنزیا «وصل» می‌شد ولی داده رد نمی‌کرد.** سنجش و بررسی وصل شدن حالا یک درخواست HTTPS واقعی از داخل خود تونل است، پس سروری که فقط پینگ می‌دهد دیگر «وصل» حساب نمی‌شود.

### کدام فایل را دانلود کنم؟
- **arm64-v8a:** بیشتر گوشی‌ها (۶۴ بیتی). اگر نمی‌دانید، همین را بگیرید.
- **armeabi-v7a:** گوشی‌های قدیمی‌تر ۳۲ بیتی.
- **universal:** روی همهٔ گوشی‌ها نصب می‌شود، ولی حجمش بیشتر است.
- به‌روزرسانی از داخل خود برنامه فایل درستِ گوشی شما را خودش برمی‌دارد.





## Exclave — `ExclaveNetwork/Exclave`
### 0.17.70 (Stable)
- Tag: `0.17.70`
- تاریخ انتشار: 2026-11-23T14:00:56Z
- صفحه رسمی: https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.70
- APKهای ARM64:
  - [Exclave-0.17.70-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.70/Exclave-0.17.70-arm64-v8a.apk)
  - [Exclave-0.17.70-legacy-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.70/Exclave-0.17.70-legacy-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
- Fix regressions introduced in the previous version.
- Change the name of the Quick Settings tile to app name.

### 0.17.69 (Stable)
- Tag: `0.17.69`
- تاریخ انتشار: 2026-11-22T13:51:23Z
- صفحه رسمی: https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.69
- APKهای ARM64:
  - [Exclave-0.17.69-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.69/Exclave-0.17.69-arm64-v8a.apk)
  - [Exclave-0.17.69-legacy-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.69/Exclave-0.17.69-legacy-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
- Improve file verification of the route asset updater (by [@lingyicute](https://github.com/lingyicute)). Before replacing the old files, for preset route asset providers, SHA-256 checksum is verified; for all files, the basic file structure is validated.
- Publish shortcuts dynamically to better work with some automation tools (#516, by [@lingyicute](https://github.com/lingyicute)).
- Many fixes for share link import and export (by [@lingyicute](https://github.com/lingyicute)).
- Fix connection failure caused by clearing the cache of the app.
- Fix some REALITY fingerprint values in UI not matching with the actual values.

### 0.17.68 (Stable)
- Tag: `0.17.68`
- تاریخ انتشار: 2026-11-10T18:07:03Z
- صفحه رسمی: https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.68
- APKهای ARM64:
  - [Exclave-0.17.68-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.68/Exclave-0.17.68-arm64-v8a.apk)
  - [Exclave-0.17.68-legacy-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.68/Exclave-0.17.68-legacy-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
- Update Go to 1.27.4 and ML-DSA is no longer advertised in `signature_algorithm_cert` in TLS Client Hello. Exclave's non-uTLS REALITY implementation also no longer advertises ML-DSA in `signature_algorithm_cert` to match the behavior of Go TLS.
- Update uTLS to latest commit and fingerprint "Chrome" now matches Chrome 155. uTLS latest commit requires Go 1.27, so Go 1.26 support is dropped and compiling Exclave now requires at least Go 1.27.
- For Snell protocol, domain address is no longer resolved to IP when sending UDP packets.
- Update Mozilla CA certificate store and 6 CA certificates are removed.
- The memory usage of rule matcher is reduced (maybe).

### 0.17.67 (Stable)
- Tag: `0.17.67`
- تاریخ انتشار: 2026-11-05T12:14:56Z
- صفحه رسمی: https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.67
- APKهای ARM64:
  - [Exclave-0.17.67-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.67/Exclave-0.17.67-arm64-v8a.apk)
  - [Exclave-0.17.67-legacy-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.67/Exclave-0.17.67-legacy-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
- Ignore certificates that can't be parsed by Go in AndroidCAstore (e.g. certificates with [negative serial number](https://crt.sh/?q=28903A635B5280FAE6774C0B6DA7D6BAA64AF2E8)).
- Fix chain proxy with the combination of some protocols unable to connect.
- Add [developer options](https://github.com/ExclaveNetwork/Exclave/wiki/Experiments) to set GODEBUG and environment variables for the Go library. They are set after Go runtime initialization, therefore not all GODEBUG and environment variables can take effect.
- Re-enable R8 optimizations for the legacy flavor.
- Update Java version from 21 to 25.

---

About CVE-2026-98432 ([NVD](https://nvd.nist.gov/vuln/detail/cve-2026-98432), [golang-announce](https://groups.google.com/g/golang-announce/c/PCoQcdxoScw)):

- Almost all the Linux kernels used by Android devices come without MPTCP support, so it is a no-op to disable MPTCP.
- Mitigating the vulnerability by disabling MPTCP is not the appropriate way. While the demonstrated exploit requires MPTCP, the underlying bug resides within TCP and is not specific to MPTCP. The fix for this vulnerability is to upgrade to a patched kernel version. Even if this vulnerability can be mitigated by disabling MPTCP, an outdated kernel is still vulnerable to tons of other RCE vulnerabilities.
- Therefore, Exclave will not explicitly disable MPTCP like many other proxy software and network tools written in Go.
- If you did compile the kernel with MPTCP support, or you insist that MPTCP must be explicitly disabled like some other Go-written software, set the related GODEBUG value through developer options yourself.

### 0.17.66 (Stable)
- Tag: `0.17.66`
- تاریخ انتشار: 2026-10-26T13:50:32Z
- صفحه رسمی: https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.66
- APKهای ARM64:
  - [Exclave-0.17.66-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.66/Exclave-0.17.66-arm64-v8a.apk)
  - [Exclave-0.17.66-legacy-arm64-v8a.apk](https://github.com/ExclaveNetwork/Exclave/releases/download/0.17.66/Exclave-0.17.66-legacy-arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
- Fix high CPU usage after proxy closed or network switching for Hysteria 2 (maybe other QUIC-based protocols too).
- Fix connections not closed correctly on proxy closed.
- Fix the `/proc/net/` based UID dumper on Android 9 or earlier (similar to https://github.com/SagerNet/sing-box/commit/40bc411e8d024e3f8c8f435c2a2ad5e4c0e04bce).

## ArasClient — `ArasTey/ArasClient`
### ArasClient 1.9.0 (Stable)
- Tag: `v1.9.0`
- تاریخ انتشار: 2026-11-22T16:16:23Z
- صفحه رسمی: https://github.com/ArasTey/ArasClient/releases/tag/v1.9.0
- APKهای ARM64:
  - [ArasClient_1.9.0_arm64-v8a.apk](https://github.com/ArasTey/ArasClient/releases/download/v1.9.0/ArasClient_1.9.0_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
# ArasClient 1.9.0

These APKs were compiled and signed by this workflow run, from the
pinned sources — not copied off a developer machine. Take the file
that matches your phone; the universal build installs anywhere and is
the largest.

## What changed

Since `v1.8.97`:

### New
- Four app themes, picked during onboarding and switchable in Settings
- First-run coach-mark guide that spotlights the real controls instead of text pages
- Jalali (Persian) dates for subscription expiry

### Improved
- Subscription tab rail and two-column config cards rebuilt in the PattNG style
- Ping results are color-coded by delay; tap the stop icon to cancel a running test
- Bottom bar text shrinks to fit instead of truncating
- Unified corner radius across cards and bars; cleaner menus and insets
- Inter + Dastkhat typography

### Under the hood
- New xray core (patterniha v26.11.21) with Serverless-for-Iran v62 support
- Rebuilt native libraries: libaether 2.4.0 and the hev socks tunnel 2.20.0, with the JNI package-name fix and a hardened tun2socks start that can no longer kill the VPN process
- The whole release is now compiled and signed by GitHub Actions from pinned sources

## Install

1. Download the APK for your architecture (`arm64-v8a` fits most modern phones).
2. Allow installs from unknown sources for the app you downloaded with.
3. Install. An existing ArasClient is upgraded in place: the signing key has not changed.

The in-app updater downloads these same files, so a release without
its assets leaves people on the old version until they are attached.

## Build information

| | |
|---|---|
| versionName | `1.9.0` |
| versionCode | `1900` (per-ABI builds use +1..+4) |
| commit | `1b7664df49c9923a41877073c3cfba37d282e300` |
| xray core | `ArasTey/xray-core@aras-core-26.11.21` |
| core bindings | `ArasTey/AndroidLibXrayLite@33f200abc13762b5c79a11597f2273fdef1d21e7` |
| Go / JDK / NDK | `1.27` / `17` / `27.2.12479018` |
| signing certificate | `3b2a6fa9c328d002ff737976a7b384423ad844346927d208052bb49ed920b5ba` |
| build run | [45041139883](https://github.com/ArasTey/ArasClient/actions/runs/45041139883) |

## Checksums

```
1d9679766e30b37fcb9b296c7dc44e0e41b2693aeba9b01476b16c413ea3b2e6  ArasClient_1.9.0_arm64-v8a.apk
4b4ebfb35505b23ed33a1ab348d5a2a5e7176ef34c78250fbe3309dd2ed90f6e  ArasClient_1.9.0_armeabi-v7a.apk
0e0953d3feafa590ab77b46d5c27fe72733646e00f7a1b56fd991b17d374e67f  ArasClient_1.9.0_x86_64.apk
47d3211d62ad4ab00d750eb4b8b9d68365b9691024fa0849ff86c86bf93da986  ArasClient_1.9.0_x86.apk
739af586464c73cdc8e545a3161c8dae344b10c983ab042119da68dfe115fdd9  ArasClient_1.9.0_universal.apk
```



### ArasClient v1.8.97 (Stable)
- Tag: `v1.8.97`
- تاریخ انتشار: 2026-11-16T23:41:14Z
- صفحه رسمی: https://github.com/ArasTey/ArasClient/releases/tag/v1.8.97
- APKهای ARM64:
  - [ArasClient_1.8.97_arm64-v8a.apk](https://github.com/ArasTey/ArasClient/releases/download/v1.8.97/ArasClient_1.8.97_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
## Changes since v1.8.95

### New: IKEv2 protocol
- Added platform IKEv2 as a full protocol: manual profiles, editor, import and share (`ikev2://` links and subscription entries), and connection through Android's VpnManager.
- IKEv2 profiles support CA certificates for server verification.
- Fixed `ikev2://` subscription imports that previously failed to connect.

### Subscription panel
- Subscription cards now show a real, fresh ping while disconnected (socket round-trip measurement) instead of a stored value.
- Unlimited subscriptions (no traffic cap) now show their used traffic as "used · Unlimited" instead of hiding the line entirely.
- The announcement banner now appears whenever the subscription provides one, and its bell toggle stays in sync with the Settings screen and across subscription tabs.
- Translated the new labels into all shipped languages.

Validation: unit tests passed, release lint and build passed, and IKEv2 end-to-end (CA + real traffic), ping display, announcement toggle, and unlimited traffic display were verified on an Android emulator.

Signed APKs are built and attached by GitHub Actions. Downloads will appear after the release workflow finishes.

### ArasClient v1.8.95 (Stable)
- Tag: `v1.8.95`
- تاریخ انتشار: 2026-11-11T16:36:16Z
- صفحه رسمی: https://github.com/ArasTey/ArasClient/releases/tag/v1.8.95
- APKهای ARM64:
  - [ArasClient_1.8.95_arm64-v8a.apk](https://github.com/ArasTey/ArasClient/releases/download/v1.8.95/ArasClient_1.8.95_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
## Changes since v1.8.92

- Fixed rectangular backgrounds behind floating input labels, including remarks and dropdown fields, in light and dark themes.
- Enabled IPv6 and Prefer IPv6 by default, including IPv6 preference when resolving domain names.
- Enabled FakeDNS and its local DNS prerequisite by default.
- Preserved explicitly saved settings: existing disabled choices are not overwritten.
- Added regression tests for network defaults and settings reset behavior.

Validation: 379 unit tests passed, release lint and build passed, and form labels and network switches were checked on an Android emulator.

Signed APKs are built and attached by GitHub Actions. Downloads will appear after the release workflow finishes.

### ArasClient v1.8.92 (Stable)
- Tag: `v1.8.92`
- تاریخ انتشار: 2026-11-09T19:46:24Z
- صفحه رسمی: https://github.com/ArasTey/ArasClient/releases/tag/v1.8.92
- APKهای ARM64:
  - [ArasClient_1.8.92_arm64-v8a.apk](https://github.com/ArasTey/ArasClient/releases/download/v1.8.92/ArasClient_1.8.92_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
## ArasClient v1.8.92

Everything since v1.8.76 — the 1.8.90 / 1.8.91 rounds plus this fix.

- **Aether gool/mim fixed** — a scan now fills the main address and port with the outer gateway and immediately sets the usual `Aether > gool` / `Aether > mim` remark on a nameless profile, so a scanned two-hop tunnel saves and shows up on its card like any other profile; two-hop links fill the same fields
- **Instant delay results** — each config's ping result appears the moment its own test ends, and delay tests run concurrently instead of one at a time
- **Verified-only country** — the flag and country on a card appear only after a successful ping and real data through that config
- **Subscription bar** — a working sort-by-test-results button, and the 3-dot menu trimmed to the actions that still apply
- **Settings** — a toggle to show or hide the smart-connect button
- **First run** — no startup questions, new defaults applied directly
- **Updater** — when the GitHub API is rate-limited, the update check falls back to the release page
- **Psiphon** — refreshed bundled server list

> Persian build, Xray core from the aras-core-26.11.1 set. Signed with the same key as v1.8.6 — installs straight over it.

### ArasClient v1.8.76 (Stable)
- Tag: `v1.8.76`
- تاریخ انتشار: 2026-11-03T20:44:48Z
- صفحه رسمی: https://github.com/ArasTey/ArasClient/releases/tag/v1.8.76
- APKهای ARM64:
  - [ArasClient_1.8.76_arm64-v8a.apk](https://github.com/ArasTey/ArasClient/releases/download/v1.8.76/ArasClient_1.8.76_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
## ArasClient v1.8.76

Everything since v1.8.6 in one release — the 1.8.7 / 1.8.71 / 1.8.75 rounds plus this round's work.

- **Glass UI rework** — frosted top bar and subscription rail over a handcrafted film-grain background, redesigned connect dial with a connecting indicator, blue selected subscription tab, uniform selected-card ring, cleaner menus, icons and dropdowns across the app, no shadows or gradients on surfaces
- **Standalone Psiphon and Tor editors** — create Psiphon and Tor profiles by hand, with auto free listen ports and webtunnel bridge support for Tor
- **Custom config support** — mihomo, sing-box and Xray JSON import, plus anti-phishing, anti-leak and CAPTCHA routing rules; Clash YAML imports skip unsupported proxies and tolerate mihomo quirks (socks5, raw, xhttp, blank fields)
- **Free configs** — delete with restore, still display-only per the 1.8.6 choice
- **Bottom bar** — egress country/IP line, stable info while connected, meaningful delay results for local configs
- **Subscription rail** — config count and long names, expiry date and announcements toggle, chain label for Aether > masque > psiphon cards
- **In-app updates** — the app checks GitHub for new releases, downloads and installs the APK itself, and applies delta patches on device when one is available for the installed version, falling back to the full APK otherwise
- **Xray core 26.11.1** — bundled core rebased onto patterniha v26.11.1; imports that need a newer core show a warning instead of failing silently
- **Serverless-for-Iran v5.6 / v5.7** — full-JSON CUSTOM configs with fragment (fragA/fragB) and TCP urgent-data (oob) transports verified end-to-end; delay probes for masked configs now try the second endpoint and measure through the live tunnel, so the cards and the bottom bar agree
- **Editor polish** — Aether editor keeps its original layout with auto-fetched keys and an IPv4+IPv6 default, friendly auto-names for Psiphon/Tor/Aether profiles, MASQUE base transport defaults to HTTP/2, delay-test spinner scoped to the card being tested, Latin digits everywhere

> Persian build, Xray core from the aras-core-26.11.1 set. Signed with the same key as v1.8.6 — installs straight over it.


## Shroudly — `umutxyp/Shroudly`
### Shroudly v2.6.90 (Stable)
- Tag: `v2.6.90`
- تاریخ انتشار: 2026-11-23T18:44:02Z
- صفحه رسمی: https://github.com/umutxyp/Shroudly/releases/tag/v2.6.90
- APKهای ARM64:
  - [Shroudly-2.6.90-Android-arm64.apk](https://github.com/umutxyp/Shroudly/releases/download/v2.6.90/Shroudly-2.6.90-Android-arm64.apk)

**یادداشت توسعه‌دهنده:**
## Shroudly 2.6.90

**The last way out (Tor) is off until you allow it, on every system and in every store edition.**

### Windows, macOS, Linux, Android, Android TV, the Mac App Store app
- "When nothing else works: the Tor network" no longer shows on from the first start. Tor never carried anything before the user said yes, but the switch looked as if it was on; it now shows what the user chose.
- Nothing is lost for anyone who chose before: with no stored choice, the switch is on only where Tor was allowed earlier ("Use Tor" on the card, or the switch turned on).
- Everyone else is asked when a site that no technique opens needs Tor, as after a "No": at most once a day for the same site, and the answer is kept.
- With the switch off, a problem report is no longer sent through Tor by itself on networks that block Cloudflare; with it on, it is sent as before.
- iPhone, iPad and Apple TV have no Tor; nothing changes there.

### Tests
- `tests/net/tor-ask.test.js` checks that no part of the desktop app takes "on" when nothing is stored, that the switch shows on only when it is on, that a report says "off" for nothing stored, that Android (`TorRoute.enabled`) and Apple (`Settings`) fall back to the earlier "allowed" answer, and that with the switch off a site nothing opens is asked about. Apple's own tests (`TorRouteTests`, `ReportTests`) and Android's unit tests pass with the new default.

### Downloads
| OS | Intel / AMD (x64) | ARM |
|----|-------------------|-----|
| Windows 10 / 11 | `Shroudly-2.6.90-Windows-x64-Setup.exe` · 32-bit: `Shroudly-2.6.90-Windows-ia32-Setup.exe` | `Shroudly-2.6.90-Windows-arm64-Setup.exe` |
| **Windows 7 / 8 / 8.1** | `Shroudly-2.6.90-Windows7-8-Setup.exe` (32- and 64-bit) | |
| macOS 12+ | `Shroudly-2.6.90-macOS-x64.dmg` (Intel) | `Shroudly-2.6.90-macOS-arm64.dmg` (Apple Silicon) |
| Debian / Ubuntu | `Shroudly-2.6.90-Linux-amd64.deb` | `Shroudly-2.6.90-Linux-arm64.AppImage` |
| Arch / Manjaro | `Shroudly-2.6.90-Linux-x64.pacman` | AppImage |
| Fedora / openSUSE / RHEL | `Shroudly-2.6.90-Linux-x86_64.rpm` | AppImage |
| Any distribution | `Shroudly-2.6.90-Linux-x86_64.AppImage` | `Shroudly-2.6.90-Linux-arm64.AppImage` |
| 32-bit ARM (armhf) | | `Shroudly-2.6.90-Linux-armv7l.AppImage` · `Shroudly-2.6.90-Linux-armv7l.deb` |
| **Android 8+, Android TV, Google TV** | `Shroudly-2.6.90-Android.apk` (one APK for every device) | same |
| Android, smaller | `Shroudly-2.6.90-Android-arm64.apk` (64-bit ARM phones only, most of them) · `Shroudly-2.6.90-Android-lite.apk` (every phone, without Tor) | same |
| **iPhone / iPad (iOS 16+), Mac, Apple TV (tvOS 17+)** | | App Store: Mac 2.6.87 (2.6.90 in review), iPhone/iPad 2.6.82 in review; 2.6.90 with the TestFlight testers; `Shroudly-2.6.90-iOS.ipa` for TrollStore |
| **Google Play** (Android, Android TV) | [Get it on Google Play](https://play.google.com/store/apps/details?id=me.codeshare.shroudly) | same |
| **A Linux server** | [one line](https://github.com/umutxyp/Shroudly#on-a-server) | same |


### Shroudly v2.6.89 (Stable)
- Tag: `v2.6.89`
- تاریخ انتشار: 2026-11-22T23:40:52Z
- صفحه رسمی: https://github.com/umutxyp/Shroudly/releases/tag/v2.6.89
- APKهای ARM64:
  - [Shroudly-2.6.89-Android-arm64.apk](https://github.com/umutxyp/Shroudly/releases/download/v2.6.89/Shroudly-2.6.89-Android-arm64.apk)

**یادداشت توسعه‌دهنده:**
## Shroudly 2.6.89

**"Your own server" takes VLESS and Trojan links, on every platform.**

### Every platform (Windows, macOS, Linux, Android, Android TV, iPhone, iPad, the Mac App Store app, Apple TV)
- Your own server now takes `vless://` and `trojan://` links, the kinds people in Iran pass around, where Shadowsocks is filtered by its look (asked for from Iran, with a link to a server behind a CDN). Carried over plain TCP, a WebSocket or HTTPUpgrade, with TLS or without; `host`, `sni`, `path` and `alpn` are read from the link, and Xray's `?ed=` note is taken off the path. Shroudly has no servers of its own: the server is the user's, as with Shadowsocks.
- A link that asks for something not carried is told so by its name, never tried another way: REALITY, the XTLS Vision flow, gRPC, XHTTP, mKCP, VLESS's own encryption.
- The server's certificate is checked for the name the link gives (its `sni`, or its `Host`, or its address). A certificate that is not valid for it is refused and said as that. `allowInsecure=1` is followed on the desktop only; on phones, tablets and Apple devices such a link is refused with its name.
- The saved link is shown with its key covered, and the log never has it.

### Windows, macOS, Linux (updates)
- An update (about 100 MB) is no longer downloaded by itself while the Roblox player is open or a full-screen program is in front. On a thin line it took the whole line for minutes, and a game's delay went from tens of milliseconds to seconds "out of nowhere" (a report from an ADSL line, 13 Mbit/s down). It is looked at again at each check, so the download comes once the game is over; "Check for updates" by hand downloads at once, as before.

### Every platform (the engine)
- Plain HTTP: the technique that rewrites the Host header writes it in mixed case (`hOsT:`) instead of all lower case (`host:`). A filter that looks for `Host:` often looks for `host:` too, which every HTTP/2 client writes: Vietnam's resets both and lets the mixed case through (measured from a Vietnamese line on 2026-11-22, where the technique opened none of four blocked sites before and all four after). Every one of 96 large web servers answered the mixed case exactly as the usual one.

### Tests
- The headers are the same bytes on every platform (`tests/net/fixtures/vless-vectors.json`, read by the desktop's, Android's and Apple's tests). Each platform carries connections through a server of each kind written in its tests (TCP, WebSocket, HTTPUpgrade; the desktop and Android also with TLS); Apple's TLS is tried against a real site by its name, by its address with the name in `sni`, and under a name its certificate is not for.
- The Windows lab's stand-in DNS forwarder takes a port the system picks and is waited for: on a port of the lab's choosing it sometimes never came up, and the DNS gate was reported as not answering.

### Downloads
| OS | Intel / AMD (x64) | ARM |
|----|-------------------|-----|
| Windows 10 / 11 | `Shroudly-2.6.89-Windows-x64-Setup.exe` · 32-bit: `Shroudly-2.6.89-Windows-ia32-Setup.exe` | `Shroudly-2.6.89-Windows-arm64-Setup.exe` |
| **Windows 7 / 8 / 8.1** | `Shroudly-2.6.89-Windows7-8-Setup.exe` (32- and 64-bit) | |
| macOS 12+ | `Shroudly-2.6.89-macOS-x64.dmg` (Intel) | `Shroudly-2.6.89-macOS-arm64.dmg` (Apple Silicon) |
| Debian / Ubuntu | `Shroudly-2.6.89-Linux-amd64.deb` | `Shroudly-2.6.89-Linux-arm64.AppImage` |
| Arch / Manjaro | `Shroudly-2.6.89-Linux-x64.pacman` | AppImage |
| Fedora / openSUSE / RHEL | `Shroudly-2.6.89-Linux-x86_64.rpm` | AppImage |
| Any distribution | `Shroudly-2.6.89-Linux-x86_64.AppImage` | `Shroudly-2.6.89-Linux-arm64.AppImage` |
| 32-bit ARM (armhf) | | `Shroudly-2.6.89-Linux-armv7l.AppImage` · `Shroudly-2.6.89-Linux-armv7l.deb` |
| **Android 8+, Android TV, Google TV** | `Shroudly-2.6.89-Android.apk` (one APK for every device) | same |
| Android, smaller | `Shroudly-2.6.89-Android-arm64.apk` (64-bit ARM phones only, most of them) · `Shroudly-2.6.89-Android-lite.apk` (every phone, without Tor) | same |
| **iPhone / iPad (iOS 16+), Mac, Apple TV (tvOS 17+)** | | App Store: Mac 2.6.84 (2.6.87 in review), iPhone/iPad 2.6.82 in review; 2.6.89 with the TestFlight testers; `Shroudly-2.6.89-iOS.ipa` for TrollStore |
| **Google Play** (Android, Android TV) | [Get it on Google Play](https://play.google.com/store/apps/details?id=me.codeshare.shroudly) | same |
| **A Linux server** | [one line](https://github.com/umutxyp/Shroudly#on-a-server) | same |


### Shroudly v2.6.88 (Stable)
- Tag: `v2.6.88`
- تاریخ انتشار: 2026-11-22T12:35:18Z
- صفحه رسمی: https://github.com/umutxyp/Shroudly/releases/tag/v2.6.88
- APKهای ARM64:
  - [Shroudly-2.6.88-Android-arm64.apk](https://github.com/umutxyp/Shroudly/releases/download/v2.6.88/Shroudly-2.6.88-Android-arm64.apk)

**یادداشت توسعه‌دهنده:**
## Shroudly 2.6.88

**Windows: Advanced mode asks for the administrator's permission once, not at every start of the computer; Games and apps mode comes on even when Windows is slow at startup; an antivirus that blocks PowerShell no longer gets it started over and over.**

### Windows (Advanced mode)
- Every start of the Advanced engine was a permission prompt (UAC, "shroudly-core-adv.exe"): at every start of the computer, and again whenever the engine had ended. Since 2.6.87 a game or a Stop no longer ends it; now the prompt itself is answered once. The engine started through it copies itself and WinDivert's files to `Common Files\Shroudly\advanced`, a folder only an administrator can write, and registers a scheduled task that runs that copy for this user only, on demand. From then on Shroudly starts Advanced mode through the task, with no prompt. It asks again, once, only after an update that changed the engine, or when the task is gone; whatever goes wrong on this way (a policy, an antivirus) ends in the prompt, as before.
- What the engine started this way does is not the caller's to say: it takes its options from a request file and accepts only the packet options, each checked; it writes its status only into its own folder, a new file every time; in the user's folder it only reads. Uninstalling Shroudly removes the task and the copies.
- The engine opens no console window of its own.
- A prompt nobody answered for three minutes (the computer started with no one at it) is said as that; it used to read "Advanced mode failed: #< CLIXML".

### Windows (Games and apps mode, Roblox)
- On a computer still starting up, with an antivirus looking at every new program, Windows' registry tool took longer than its four seconds, and Games and apps mode was refused for the whole session ("this session has no volatile environment"): Roblox opened with no way to the internet ("critical settings could not be downloaded", a report from Türkiye). The engine now reads and writes those settings itself when the tool does not answer in time (after two such waits the tool is not tried again in that run), and where even that fails the mode is tried again by itself after 8 s, 30 s, 90 s and 5 minutes.
- An antivirus that blocks PowerShell's command line (Avast) showed its warning over and over: a Roblox program being judged was asked about every two seconds, each time in a new PowerShell. After four questions in a row without an answer none is started for ten minutes, then for longer and longer, until it answers again; said once in the log.

### Windows, macOS (Games and apps mode)
- NO_PROXY no longer ends with the IPv6 ranges `fc00::/7` and `fe80::/10`: Python's httpx reads each entry as a URL and failed on them ("Invalid port: ':'"), so Unsloth Studio and every tool built on httpx would not start while the mode was on (#96). The value an earlier version wrote is replaced when the mode comes on, and still removed as ours.

### Windows, macOS, Linux
- A computer that does not let Shroudly create files (a cleaning program that removed the temporary folder, folders protected against new files): the temporary folder is made again, and what was refused is said once with what to do, instead of "ENOENT" at every step.

### Downloads
| OS | Intel / AMD (x64) | ARM |
|----|-------------------|-----|
| Windows 10 / 11 | `Shroudly-2.6.88-Windows-x64-Setup.exe` · 32-bit: `Shroudly-2.6.88-Windows-ia32-Setup.exe` | `Shroudly-2.6.88-Windows-arm64-Setup.exe` |
| **Windows 7 / 8 / 8.1** | `Shroudly-2.6.88-Windows7-8-Setup.exe` (32- and 64-bit) | |
| macOS 12+ | `Shroudly-2.6.88-macOS-x64.dmg` (Intel) | `Shroudly-2.6.88-macOS-arm64.dmg` (Apple Silicon) |
| Debian / Ubuntu | `Shroudly-2.6.88-Linux-amd64.deb` | `Shroudly-2.6.88-Linux-arm64.AppImage` |
| Arch / Manjaro | `Shroudly-2.6.88-Linux-x64.pacman` | AppImage |
| Fedora / openSUSE / RHEL | `Shroudly-2.6.88-Linux-x86_64.rpm` | AppImage |
| Any distribution | `Shroudly-2.6.88-Linux-x86_64.AppImage` | `Shroudly-2.6.88-Linux-arm64.AppImage` |
| 32-bit ARM (armhf) | | `Shroudly-2.6.88-Linux-armv7l.AppImage` · `Shroudly-2.6.88-Linux-armv7l.deb` |
| **Android 8+, Android TV, Google TV** | `Shroudly-2.6.88-Android.apk` (one APK for every device) | same |
| Android, smaller | `Shroudly-2.6.88-Android-arm64.apk` (64-bit ARM phones only, most of them) · `Shroudly-2.6.88-Android-lite.apk` (every phone, without Tor) | same |
| **iPhone / iPad (iOS 16+), Mac, Apple TV (tvOS 17+)** | | App Store: Mac 2.6.84 (2.6.87 in review), iPhone/iPad 2.6.82 in review; 2.6.88 with the TestFlight testers; `Shroudly-2.6.88-iOS.ipa` for TrollStore |
| **Google Play** (Android, Android TV) | [Get it on Google Play](https://play.google.com/store/apps/details?id=me.codeshare.shroudly) | same |
| **A Linux server** | [one line](https://github.com/umutxyp/Shroudly#on-a-server) | same |


### Shroudly v2.6.87 (Stable)
- Tag: `v2.6.87`
- تاریخ انتشار: 2026-11-20T13:22:13Z
- صفحه رسمی: https://github.com/umutxyp/Shroudly/releases/tag/v2.6.87
- APKهای ARM64:
  - [Shroudly-2.6.87-Android-arm64.apk](https://github.com/umutxyp/Shroudly/releases/download/v2.6.87/Shroudly-2.6.87-Android-arm64.apk)

**یادداشت توسعه‌دهنده:**
## Shroudly 2.6.87

**Advanced mode no longer asks for the administrator's permission again after a game or a Stop and Start; a site the last way out (Tor) does not reach no longer waits on it.**

### Windows and Linux (Advanced mode)
- Advanced mode stepped aside for a game's anti-cheat, or for the user's Stop, by ending its elevated engine, so coming back asked for the administrator's permission every time (a "shroudly-core" prompt after each game). Now it goes on standby instead: the packet hook let go and the WinDivert driver unloaded, so the anti-cheat sees no driver as before, while the engine waits; coming back takes the hook again with no prompt. Turned off by hand, at quit and before an update it stops for good, as before; an engine that cannot come back is started anew (one prompt). On Linux the same with the firewall rules and pkexec's password.

### Every system with the last way out (Windows, macOS, Linux, Android, the Mac App Store app)
- A name sent to the last way out first (the user's Tor list, or a name the network keeps cutting) waited up to 45 seconds on Tor at every connection when Tor was running but could not reach it, and an app gave up first (a report from India: Roblox Studio stuck at "Setting up server"). After two such misses the name goes the usual way at once for ten minutes, said once in the log.

### Downloads
| OS | Intel / AMD (x64) | ARM |
|----|-------------------|-----|
| Windows 10 / 11 | `Shroudly-2.6.87-Windows-x64-Setup.exe` · 32-bit: `Shroudly-2.6.87-Windows-ia32-Setup.exe` | `Shroudly-2.6.87-Windows-arm64-Setup.exe` |
| **Windows 7 / 8 / 8.1** | `Shroudly-2.6.87-Windows7-8-Setup.exe` (32- and 64-bit) | |
| macOS 12+ | `Shroudly-2.6.87-macOS-x64.dmg` (Intel) | `Shroudly-2.6.87-macOS-arm64.dmg` (Apple Silicon) |
| Debian / Ubuntu | `Shroudly-2.6.87-Linux-amd64.deb` | `Shroudly-2.6.87-Linux-arm64.AppImage` |
| Arch / Manjaro | `Shroudly-2.6.87-Linux-x64.pacman` | AppImage |
| Fedora / openSUSE / RHEL | `Shroudly-2.6.87-Linux-x86_64.rpm` | AppImage |
| Any distribution | `Shroudly-2.6.87-Linux-x86_64.AppImage` | `Shroudly-2.6.87-Linux-arm64.AppImage` |
| 32-bit ARM (armhf) | | `Shroudly-2.6.87-Linux-armv7l.AppImage` · `Shroudly-2.6.87-Linux-armv7l.deb` |
| **Android 8+, Android TV, Google TV** | `Shroudly-2.6.87-Android.apk` (one APK for every device) | same |
| Android, smaller | `Shroudly-2.6.87-Android-arm64.apk` (64-bit ARM phones only, most of them) · `Shroudly-2.6.87-Android-lite.apk` (every phone, without Tor) | same |
| **iPhone / iPad (iOS 16+), Mac, Apple TV (tvOS 17+)** | | App Store: iPhone/iPad 2.6.82 in review, Mac 2.6.84 in review; 2.6.87 with the TestFlight testers; `Shroudly-2.6.87-iOS.ipa` for TrollStore |
| **Google Play** (Android, Android TV) | [Get it on Google Play](https://play.google.com/store/apps/details?id=me.codeshare.shroudly) | same |
| **A Linux server** | [one line](https://github.com/umutxyp/Shroudly#on-a-server) | same |


### Shroudly v2.6.86 (Stable)
- Tag: `v2.6.86`
- تاریخ انتشار: 2026-11-20T05:07:56Z
- صفحه رسمی: https://github.com/umutxyp/Shroudly/releases/tag/v2.6.86
- APKهای ARM64:
  - [Shroudly-2.6.86-Android-arm64.apk](https://github.com/umutxyp/Shroudly/releases/download/v2.6.86/Shroudly-2.6.86-Android-arm64.apk)

**یادداشت توسعه‌دهنده:**
## Shroudly 2.6.86

**Apps with a protocol of their own that no technique opens (Telegram in Jordan) go through the last way out (Tor); Advanced mode gives a site cut after its first kilobytes the stronger way before Tor, and says which servers got it.**

### Every system with the last way out (Windows, macOS, Linux, Android, the Mac App Store app)
- A destination of an app's own protocol (not TLS or HTTP: Telegram, straight to its addresses) that every technique failed on was only left alone for a while: its connections never went to the last way out, even with Tor ready beside them (a report from Jordan: Telegram did not connect, Tor ready, nothing carried). Now its next connections go through the last way out, where it is allowed, and one not running is asked for; after ten minutes the techniques are tried again. A destination a technique opens goes exactly as before; the iPhone and iPad app has no last way out and is unchanged.

### Windows and Linux (Advanced mode)
- A connection frozen after its first 16 to 20 KB sent its site to the last way out at once, a Tor that cannot start on Rostelecom, so the stronger way 2.6.85 gives that server never had its chance (x.com and Discord stayed white). With Advanced mode on, the site goes to the last way out only if the cuts go on. Without Advanced mode, as before.
- The log says which server got the stronger way after a cut, once per address, and a report carries Advanced mode's counters (servers escalated, first segments sent the stronger way, with timestamps).

### Downloads
| OS | Intel / AMD (x64) | ARM |
|----|-------------------|-----|
| Windows 10 / 11 | `Shroudly-2.6.86-Windows-x64-Setup.exe` · 32-bit: `Shroudly-2.6.86-Windows-ia32-Setup.exe` | `Shroudly-2.6.86-Windows-arm64-Setup.exe` |
| **Windows 7 / 8 / 8.1** | `Shroudly-2.6.86-Windows7-8-Setup.exe` (32- and 64-bit) | |
| macOS 12+ | `Shroudly-2.6.86-macOS-x64.dmg` (Intel) | `Shroudly-2.6.86-macOS-arm64.dmg` (Apple Silicon) |
| Debian / Ubuntu | `Shroudly-2.6.86-Linux-amd64.deb` | `Shroudly-2.6.86-Linux-arm64.AppImage` |
| Arch / Manjaro | `Shroudly-2.6.86-Linux-x64.pacman` | AppImage |
| Fedora / openSUSE / RHEL | `Shroudly-2.6.86-Linux-x86_64.rpm` | AppImage |
| Any distribution | `Shroudly-2.6.86-Linux-x86_64.AppImage` | `Shroudly-2.6.86-Linux-arm64.AppImage` |
| 32-bit ARM (armhf) | | `Shroudly-2.6.86-Linux-armv7l.AppImage` · `Shroudly-2.6.86-Linux-armv7l.deb` |
| **Android 8+, Android TV, Google TV** | `Shroudly-2.6.86-Android.apk` (one APK for every device) | same |
| Android, smaller | `Shroudly-2.6.86-Android-arm64.apk` (64-bit ARM phones only, most of them) · `Shroudly-2.6.86-Android-lite.apk` (every phone, without Tor) | same |
| **iPhone / iPad (iOS 16+), Mac, Apple TV (tvOS 17+)** | | App Store: iPhone/iPad 2.6.82 in review, Mac 2.6.84 in review; 2.6.86 with the TestFlight testers; `Shroudly-2.6.86-iOS.ipa` for TrollStore |
| **Google Play** (Android, Android TV) | [Get it on Google Play](https://play.google.com/store/apps/details?id=me.codeshare.shroudly) | same |
| **A Linux server** | [one line](https://github.com/umutxyp/Shroudly#on-a-server) | same |


## MahsaNG — `GFW-knocker/MahsaNG`
### v18-(1405-7-10) (Stable)
- Tag: `v18-(1405-7-10)`
- تاریخ انتشار: 2026-10-02T06:52:13Z
- صفحه رسمی: https://github.com/GFW-knocker/MahsaNG/releases/tag/v18-(1405-7-10)
- APKهای ARM64:
  - [MahsaNG_18_arm64-v8a.apk](https://github.com/GFW-knocker/MahsaNG/releases/download/v18-%281405-7-10%29/MahsaNG_18_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
update core to v26.10.3-mahsa-r2
support masque:// protocol
IP scanner now support masque , wireguard and custom port
masque:// and wireguard:// config now support "auto" as a key 
utility to backup and restore personal config (no storage permission asked, use OS file chooser)
telegram proxy page with utility to copy or test single proxy
ability to "Undo Sort" by long pressing of Sort button
fragment (auto) improved
new udp noises added
new youtube (serverless) config added
cipher suite option for tls added (idea by patterniha)
finalmask option for all protocols including masque, hy2
chaining two config now support fragment , hy2 , masque
new way of fetching config from mahsaserver

UI:
significant UI improvement
all internal pages appearance refined
smooth sweep left/right to switch between subscription
add new status color in test layout

fixes:
showing ip in test layout fixed
toast no longer cover test layout
upload speed measurement in test layout fixed
showing widget text for psiphon:// config fixed
new country added to psiphon region (BR,IT,NZ)
support flat version of server address in json config
ech link params now read v2rayng standard
finalmask UI bug fixed
vmess link now carry finalmask



### v17-(1405-4-12) (Stable)
- Tag: `v17-(1405-4-12)`
- تاریخ انتشار: 2026-07-03T11:08:06Z
- صفحه رسمی: https://github.com/GFW-knocker/MahsaNG/releases/tag/v17-(1405-4-12)
- APKهای ARM64:
  - [MahsaNG_17_arm64-v8a.apk](https://github.com/GFW-knocker/MahsaNG/releases/download/v17-%281405-4-12%29/MahsaNG_17_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
this is a byte-for-byte identical of playstore version
we recommend to [update MahsaNG from playstore](https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG)


for full v17 changelog visit this:
https://github.com/GFW-knocker/MahsaNG/releases/tag/v17-(1405-4-8)


minor changes from the previous v17 version:
- text on subscription menu is now aligned center
- bypass apps internal web request (config fetch, update, ...) from psiphon vpn
- fix Drag-Shadow crash on Android 10/11 (required by google)
- increment versionCode (required by google)

### v17-(1405-4-8) (Stable)
- Tag: `v17-(1405-4-8)`
- تاریخ انتشار: 2026-07-01T16:23:34Z
- صفحه رسمی: https://github.com/GFW-knocker/MahsaNG/releases/tag/v17-(1405-4-8)
- APKهای ARM64:
  - [MahsaNG_17_arm64-v8a.apk](https://github.com/GFW-knocker/MahsaNG/releases/download/v17-%281405-4-8%29/MahsaNG_17_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
CORE:
- new psiphon core optimized for Iran
- ability to create, import, export & share psiphon:// config
- powerful IP scanner designed for psiphon cdn_fronting

APP:
- ability to receive v2ray config via google notification
- a menu for chaining two v2ray config
- a menu for deleting configs with no-ping in current sub

UI:
- new elegant User Interface
- ability to receive notification, news, update, etc
- sweep left/right to move between Subs
- better handling of large Subs
- show number of current config during test
- better multi-lingual capability
- better icons & light/dark theme

BUG FIX:
- fix psiphon reconnecting & crash problem
- fix widget behavior for psiphon
- fix psiphon-after problem when protocol is cdn-fronting
- fix arm-v7a crash & hang
- fix http manual password not restored on UI
- fix importing sub link when user on custom sub


### v16-(1405-2-25) (Stable)
- Tag: `v16-(1405-2-25)`
- تاریخ انتشار: 2026-05-16T17:20:47Z
- صفحه رسمی: https://github.com/GFW-knocker/MahsaNG/releases/tag/v16-(1405-2-25)
- APKهای ARM64:
  - [MahsaNG_16_arm64-v8a.apk](https://github.com/GFW-knocker/MahsaNG/releases/download/v16-%281405-2-25%29/MahsaNG_16_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
add [MasterDNS](https://github.com/masterking32/MasterDnsVPN) v2026.05.10
add [GooseRelay](https://github.com/Kianmhz/GooseRelayVPN) v1.6.0
add [FlowDriver](https://github.com/NullLatency/FlowDriver) v0.0.5
add Psiphon CDN-Fronting (credit [shirkhorshid](https://github.com/shirokhorshid/shirokhorshid-android) & [patterniha](https://github.com/patterniha/MITM-DomainFronting))
add Psiphon LAN sharing
add "type manually HTTP"
"psiphon-alone" now run without v2ray config
DNS scanner now shuffle ip
fix crashes related to getting config & psiphon service
fix socks bug when import from link
menu UI improved



### v15-(1405-1-22) (Stable)
- Tag: `v15-(1405-1-22)`
- تاریخ انتشار: 2026-04-12T00:09:40Z
- صفحه رسمی: https://github.com/GFW-knocker/MahsaNG/releases/tag/v15-(1405-1-22)
- APKهای ARM64:
  - [MahsaNG_15_arm64-v8a.apk](https://github.com/GFW-knocker/MahsaNG/releases/download/v15-%281405-1-22%29/MahsaNG_15_arm64-v8a.apk)

**یادداشت توسعه‌دهنده:**
- update mahsa-core to v26.3.31
- add Dnstt & xdns support
- add Psiphon + Conduit support (thanks to [Samim](https://x.com/pawntopromotion) for adding psiphon core)
- ability to select country for psiphon
- ability to run psiphon alone or chain after some v2ray config (using F menu)
- add DNS-scanner tool
- much improvement for navigation on TV 
- add speed test in main screen
- add dns-backup configs in EMS menu
- ability to update sub through vpn
- ability to limit dnstt configs to telegram or github
- adoption for android edge-to-edge aand 16KB device


## موارد در انتظار تأیید کاربر

- BPB VPN — `v1.3.0` — Stable — https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.3.0
- BPB VPN — `v1.2.2` — Pre-release — https://github.com/bia-pain-bache/BPB-VPN/releases/tag/v1.2.2
- PattNG — `2.4.0-P73` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.4.0-P73
- PattNG — `2.4.0-P72` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.4.0-P72
- PattNG — `2.3.15-P71` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.3.15-P71
- PattNG — `2.3.13-P70` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.3.13-P70
- PattNG — `2.3.13-P69` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.3.13-P69
- PattNG — `2.3.13-P68` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.3.13-P68
- PattNG — `2.3.12-P67` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.3.12-P67
- Karing — `v1.2.26.2934` — Stable — https://github.com/KaringX/karing/releases/tag/v1.2.26.2934
- MLM VPN — `v1.2.49` — Stable — https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.49
- MLM VPN — `v1.2.48` — Stable — https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.48
- MLM VPN — `v1.2.47` — Stable — https://github.com/mlmvpn/mlmvpn_android/releases/tag/v1.2.47
- Exclave — `0.17.69` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.69
- Exclave — `0.17.68` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.68
- Exclave — `0.17.67` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.67
- Exclave — `0.17.66` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.66
- Exclave — `0.17.64` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.64
- Exclave — `0.17.63-beta.3` — Pre-release — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.63-beta.3
- Exclave — `0.17.63-beta.1` — Pre-release — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.63-beta.1
- Exclave — `0.17.62` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.62
- Exclave — `0.17.60` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.60
- Exclave — `0.17.58` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.58
- Exclave — `0.17.57-beta.1` — Pre-release — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.57-beta.1
- Exclave — `0.17.57-beta.0` — Pre-release — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.57-beta.0
- ArasClient — `v1.9.0` — Stable — https://github.com/ArasTey/ArasClient/releases/tag/v1.9.0
- Shroudly — `v2.6.88` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.88
- Shroudly — `v2.6.87` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.87
- Shroudly — `v2.6.86` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.86
- Shroudly — `v2.6.85` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.85
- Shroudly — `v2.6.84` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.84
- Shroudly — `v2.6.83` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.83
- Shroudly — `v2.6.82` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.82
- Shroudly — `v2.6.80` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.80
- Shroudly — `v2.6.79` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.79
- Shroudly — `tor-16.0.1` — Pre-release — https://github.com/umutxyp/Shroudly/releases/tag/tor-16.0.1
- Shroudly — `v2.6.78` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.78
- Shroudly — `v2.6.77` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.77
- Shroudly — `v2.6.76` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.76
- MahsaNG — `v18-(1405-7-10)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v18-(1405-7-10)
- MahsaNG — `v17-(1405-4-12)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v17-(1405-4-12)
- MahsaNG — `v17-(1405-4-8)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v17-(1405-4-8)
- MahsaNG — `v16-(1405-2-25)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v16-(1405-2-25)
- MahsaNG — `v15-(1405-1-22)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v15-(1405-1-22)
- MahsaNG — `v14-(1404-5-30)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v14-(1404-5-30)
- MahsaNG — `v13-(1404-2-25)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v13-(1404-2-25)
- MahsaNG — `v12-(1403-11-7)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v12-(1403-11-7)
- MahsaNG — `v11-(1403-10-25)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v11-(1403-10-25)
- MahsaNG — `v10-(1403-7-25)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v10-(1403-7-25)
- MahsaNG — `v9.5-(1403-6-10)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v9.5-(1403-6-10)
- MahsaNG — `v9.0-(1403-5-30)` — Stable — https://github.com/GFW-knocker/MahsaNG/releases/tag/v9.0-(1403-5-30)
- PattNG — `2.4.0-P74` — Stable — https://github.com/patterniha/PattNG/releases/tag/2.4.0-P74
- Exclave — `0.17.70` — Stable — https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.70
- Shroudly — `v2.6.90` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.90
- Shroudly — `v2.6.89` — Stable — https://github.com/umutxyp/Shroudly/releases/tag/v2.6.89

برای ثبت آگاهی، پس از اعلام کاربر «متوجه شدم»، مورد مربوط باید از `state/pending_ack.json` حذف شود. تا پیش از آن، موارد pending در گزارش‌های بعدی تکرار می‌شوند.

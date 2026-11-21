#!/usr/bin/env python3
"""Daily metadata-only watcher for the eight configured GitHub projects."""
import json, os, re, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config/apps.json").read_text(encoding="utf-8"))
STATE = ROOT / "state"
REPORTS = ROOT / "reports"
STATE.mkdir(exist_ok=True); REPORTS.mkdir(exist_ok=True)
seen_path = STATE / "seen_releases.json"
pending_path = STATE / "pending_ack.json"
seen = json.loads(seen_path.read_text()) if seen_path.exists() else {}
pending = json.loads(pending_path.read_text()) if pending_path.exists() else {}
token = os.getenv("GITHUB_TOKEN", "")
headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"vpn-update-watch"}
if token: headers["Authorization"] = "Bearer " + token

def get_json(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=25) as res:
            return json.loads(res.read().decode("utf-8")), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.reason}"
    except Exception as e:
        return None, str(e)

def arm64_assets(assets):
    out=[]
    for a in assets or []:
        name=a.get("name","")
        if re.search(r"(arm64|arm64-v8a|aarch64)",name,re.I) and name.lower().endswith(".apk"):
            out.append({"name":name,"url":a.get("browser_download_url"),"size":a.get("size")})
    return out

results=[]
for app in CONFIG["apps"]:
    url=f"https://api.github.com/repos/{app['repo']}/releases?per_page=20"
    releases, error=get_json(url)
    item={"name":app["name"],"repo":app["repo"],"installed_version":app.get("installed_version",""),"error":error,"releases":[]}
    if releases is not None:
        valid=[r for r in releases if not r.get("draft")]
        new_for_app=[]
        baseline=app.get("installed_version","").strip().lower().replace("v","",1)
        baseline_index=None
        for idx,r in enumerate(valid):
            tag=r.get("tag_name","")
            if tag.lower().replace("v","",1)==baseline or (baseline and baseline in (r.get("name") or "").lower()):
                baseline_index=idx
            key=app["repo"]+"@"+tag
            rel={"tag":tag,"title":r.get("name") or tag,"published_at":r.get("published_at"),"prerelease":bool(r.get("prerelease")),"url":r.get("html_url"),"notes":r.get("body") or "(توضیحی در متن Release ثبت نشده است)","arm64_apks":arm64_assets(r.get("assets",[])),"assets":[{"name":a.get("name"),"url":a.get("browser_download_url"),"size":a.get("size")} for a in r.get("assets",[])]}
            item["releases"].append(rel)
            if key not in seen:
                new_for_app.append((key,rel))
            seen[key]=rel.get("published_at")
        # On the first run, compare against the user's recorded version so old
        # historical releases are not all incorrectly flagged as new.
        if new_for_app:
            if first_run:
                if baseline_index is not None:
                    candidates=[x for x in new_for_app if next((i for i,r in enumerate(valid) if r.get("tag_name")==x[1]["tag"]),999)<baseline_index]
                else:
                    candidates=new_for_app[:1]
            else:
                candidates=new_for_app
            for key,rel in candidates:
                pending[key]={"app":app["name"],"repo":app["repo"],"tag":rel["tag"],"url":rel["url"],"first_seen":datetime.now(timezone.utc).isoformat(),"prerelease":rel["prerelease"]}
    results.append(item)

now=datetime.now(timezone.utc).isoformat()
report={"checked_at_utc":now,"device":CONFIG["device"],"apps":results,"pending_ack":list(pending.values())}
(REPORTS/"latest.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
lines=["# گزارش پایش نسخه‌ها","",f"آخرین بررسی (UTC): {now}","","> فقط داده‌های رسمی GitHub گزارش می‌شود؛ این ابزار درباره نصب یا ارتقا توصیه نمی‌کند.",""]
for app in results:
    lines += [f"## {app['name']} — `{app['repo']}`"]
    if app["error"]:
        lines += [f"- خطای دریافت: {app['error']}",""]
        continue
    if not app["releases"]:
        lines += ["- در endpoint رسمی Releases موردی برنگشت؛ این به معنی نبود commit یا tag جدید نیست.",""]
        continue
    for r in app["releases"][:5]:
        kind="Pre-release" if r["prerelease"] else "Stable"
        lines += [f"### {r['title']} ({kind})",f"- Tag: `{r['tag']}`",f"- تاریخ انتشار: {r['published_at']}",f"- صفحه رسمی: {r['url']}"]
        if r["arm64_apks"]:
            lines += ["- APKهای ARM64:"]+[f"  - [{a['name']}]({a['url']})" for a in r["arm64_apks"]]
        else: lines += ["- APK با نام‌گذاری ARM64 در assets پیدا نشد."]
        lines += ["","**یادداشت توسعه‌دهنده:**",r["notes"],""]
lines += ["## موارد در انتظار تأیید کاربر",""]
if pending:
    for p in pending.values(): lines += [f"- {p['app']} — `{p['tag']}` — {'Pre-release' if p['prerelease'] else 'Stable'} — {p['url']}"]
else: lines += ["- مورد تأییدنشده‌ای ثبت نشده است."]
lines += ["","برای ثبت آگاهی، پس از اعلام کاربر «متوجه شدم»، مورد مربوط باید از `state/pending_ack.json` حذف شود. تا پیش از آن، موارد pending در گزارش‌های بعدی تکرار می‌شوند."]
(REPORTS/"latest.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
(STATE/"seen_releases.json").write_text(json.dumps(seen,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(STATE/"pending_ack.json").write_text(json.dumps(pending,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Checked {len(results)} repositories; pending acknowledgements: {len(pending)}")

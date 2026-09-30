"""Builds a VPM listing (index.json) from every GitHub release of this repository."""
import hashlib, json, os, sys, urllib.request

repo, out_dir = sys.argv[1], sys.argv[2]
owner, name = repo.split("/")
token = os.environ["GH_TOKEN"]

def get(url, accept="application/vnd.github+json"):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": accept})
    with urllib.request.urlopen(req) as r:
        return r.read()

pkg = json.load(open("package.json", encoding="utf-8"))
versions = {}
page = 1
while True:
    releases = json.loads(get(f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}"))
    if not releases:
        break
    for rel in releases:
        if rel.get("draft"):
            continue
        assets = {a["name"]: a for a in rel["assets"]}
        zips = [a for n, a in assets.items() if n.endswith(".zip")]
        if "package.json" not in assets or not zips:
            continue
        manifest = json.loads(get(assets["package.json"]["url"], "application/octet-stream"))
        data = get(zips[0]["url"], "application/octet-stream")
        manifest["url"] = zips[0]["browser_download_url"]
        manifest["zipSHA256"] = hashlib.sha256(data).hexdigest()
        versions[manifest["version"]] = manifest
    page += 1

listing = {
    "name": pkg["author"]["name"] + " VPM",
    "id": pkg["name"] + ".listing",
    "url": f"https://{owner.lower()}.github.io/{name}/index.json",
    "author": pkg["author"]["name"],
    "packages": {pkg["name"]: {"versions": versions}},
}
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
    json.dump(listing, f, indent=2)
print(f"Listed {len(versions)} version(s): {', '.join(sorted(versions))}")

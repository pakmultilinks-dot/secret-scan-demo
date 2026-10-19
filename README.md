# Secret Scanning in CI - Demo

Demo project for TechAbout task ZR-26-00755: automatic secret scanning on every push.

## What this does

Every push and pull request triggers a GitHub Actions workflow (`.github/workflows/secret-scan.yml`)
that runs [Gitleaks](https://github.com/gitleaks/gitleaks) across the full git history. If a secret
(API key, token, password, private key, etc.) is detected, the pipeline **fails** and blocks the merge.

## Files

- `.github/workflows/secret-scan.yml` - the CI workflow
- `src/app.py` - a tiny sample app (no secrets in it)
- `RUNBOOK.md` - what to do if a real secret leaks

## How it was tested

1. Pushed clean code - workflow passed (green).
2. Committed a file containing a fake AWS-style secret - workflow failed (red), proving the scan works.
3. Removed the fake secret - workflow passed again.

See the Actions tab and `RUNBOOK.md` for details.

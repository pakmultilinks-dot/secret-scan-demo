# Runbook: What to do if a real secret leaks

This guide covers the steps to take when the secret-scan pipeline fails on a **real** secret
(not a test), or when you discover a secret was committed to a repository.

## 1. Do not panic, act fast

Secrets in git history are visible to everyone with repo access. Treat it as compromised
the moment it is pushed.

## 2. Revoke and rotate the secret immediately

- Go to the provider (AWS, GitHub, Stripe, etc.) and **revoke/delete** the leaked key.
- Generate a **new** secret. Update every place that used the old one (servers, CI variables, apps).
- Revoking first is critical: removing it from git does NOT un-expose it.

## 3. Remove it from the repository

- For the latest commit only: `git reset --soft HEAD~1`, remove the secret, recommit, force-push
  (only if no one else has pulled the bad commit).
- For older history: use `git filter-repo` or the BFG Repo-Cleaner to purge the secret from
  all history, then force-push. Coordinate with the team first.
- After purging, everyone must re-clone or reset their local copies.

## 4. Check for misuse

- Review the provider's audit/access logs for the time window the secret was exposed.
- Look for unfamiliar API calls, logins, or resource changes.

## 5. Prevent it happening again

- Move the secret to a proper store: GitHub Actions Secrets, environment variables, or a
  vault (never in code or config files).
- Add the file pattern to `.gitignore` (e.g. `.env`).
- Keep this secret-scan workflow enabled on every repository so the next leak fails the build.

## 6. Report

- Tell your team lead what leaked, when, and what you rotated.
- If customer data could be affected, escalate per company policy.

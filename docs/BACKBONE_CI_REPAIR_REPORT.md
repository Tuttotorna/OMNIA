# Backbone CI Repair Report

Repository: OMNIA

Timestamp UTC: 2026-05-21T19:05:35Z

Purpose:
Repair remaining red GitHub Actions caused by missing online backbone package installation.

No release was created.
No tag was created.
Only CI workflow files and this repair report were changed.

Boundary:
measurement != inference != decision

Before:
{
  "green": false,
  "status": "failed",
  "reason": "At least one Actions run for current HEAD failed.",
  "runs": [
    {
      "id": 26246913912,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIA/actions/runs/26246913912",
      "created_at": "2026-05-21T19:00:22Z",
      "updated_at": "2026-05-21T19:00:44Z",
      "head_sha": "abafb739a0480d01dfe6f0f8c0dcc84a487354d2"
    }
  ]
}

Patch:
{
  "ci_changed": true,
  "legacy_non_dot_github_removed": [],
  "duplicate_test_workflows_removed": [],
  "python_version_policy": "3.12 only",
  "backbone_installs": {
    "OMNIA": true,
    "omnia-limit": true,
    "OMNIA-INVARIANCE": true
  },
  "required_omnia_doi_command_present": true
}

Local tests:
{
  "status": "pass",
  "passed": 57,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "57 passed in 1.47s"
}

Push:
null

After online check:
null

After failed logs:
null

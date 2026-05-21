# Second-Pass Online CI Repair Report

Repository: OMNIA

Timestamp UTC: 2026-05-21T18:58:19Z

Purpose:
Repair remaining red GitHub Actions after first ecosystem CI repair.

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
      "id": 26239387783,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIA/actions/runs/26239387783",
      "created_at": "2026-05-21T16:34:42Z",
      "updated_at": "2026-05-21T16:35:01Z",
      "head_sha": "b8ad8cb2c27961e8459cc86710999b72b1bf959c"
    }
  ]
}

Failed online log samples before repair:
{
  "ok": true,
  "failed_runs": [
    {
      "id": 26239387783,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIA/actions/runs/26239387783",
      "created_at": "2026-05-21T16:34:42Z",
      "updated_at": "2026-05-21T16:35:01Z",
      "head_sha": "b8ad8cb2c27961e8459cc86710999b72b1bf959c"
    }
  ],
  "samples": [
    {
      "run_id": 26239387783,
      "download_ok": true,
      "html_url": "https://github.com/Tuttotorna/OMNIA/actions/runs/26239387783",
      "samples": [
        {
          "file": "0_Python 3.10.txt",
          "lines": [
            "2026-05-21T16:34:49.9792161Z \u001b[36;1mpython -m pip install pytest\u001b[0m",
            "2026-05-21T16:34:53.8129677Z Collecting pytest",
            "2026-05-21T16:34:53.8671654Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T16:34:53.8823334Z Collecting exceptiongroup>=1 (from pytest)",
            "2026-05-21T16:34:53.9039836Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T16:34:53.9228289Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T16:34:53.9376047Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T16:34:53.9621445Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T16:34:53.9915265Z Collecting tomli>=1 (from pytest)",
            "2026-05-21T16:34:54.0124049Z Collecting typing-extensions>=4.6.0 (from exceptiongroup>=1->pytest)",
            "2026-05-21T16:34:54.0276235Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T16:34:54.1257266Z Installing collected packages: typing-extensions, tomli, pygments, pluggy, packaging, iniconfig, exceptiongroup, pytest",
            "2026-05-21T16:34:55.0831242Z Successfully installed exceptiongroup-1.3.1 iniconfig-2.3.0 packaging-26.2 pluggy-1.6.0 pygments-2.20.0 pytest-9.0.3 tomli-2.4.1 typing-extensions-4.15.0",
            "2026-05-21T16:34:57.3733427Z ##[group]Run python -m pytest -q tests/test_doi_ownership.py",
            "2026-05-21T16:34:57.3733887Z \u001b[36;1mpython -m pytest -q tests/test_doi_ownership.py\u001b[0m",
            "2026-05-21T16:34:57.9384825Z ##[group]Run python -m pytest -q",
            "2026-05-21T16:34:57.9385109Z \u001b[36;1mpython -m pytest -q\u001b[0m",
            "2026-05-21T16:34:58.3732334Z ==================================== ERRORS ====================================",
            "2026-05-21T16:34:58.3733419Z ___ ERROR collecting tests/test_boundary_certificate_against_omnia_limit.py ____",
            "2026-05-21T16:34:58.3734914Z ImportError while importing test module '/home/runner/work/OMNIA/OMNIA/tests/test_boundary_certificate_against_omnia_limit.py'.",
            "2026-05-21T16:34:58.3737593Z Traceback:",
            "2026-05-21T16:34:58.3742910Z E   ModuleNotFoundError: No module named 'omnia_limit'",
            "2026-05-21T16:34:58.3745123Z ERROR tests/test_boundary_certificate_against_omnia_limit.py",
            "2026-05-21T16:34:58.3746083Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T16:34:58.3746811Z 1 error in 0.25s",
            "2026-05-21T16:34:58.3966814Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "1_Python 3.12.txt",
          "lines": [
            "2026-05-21T16:34:50.2655783Z \u001b[36;1mpython -m pip install pytest\u001b[0m",
            "2026-05-21T16:34:53.4940695Z Collecting pytest",
            "2026-05-21T16:34:53.5489263Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T16:34:53.5621101Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T16:34:53.5844223Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T16:34:53.5995767Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T16:34:53.6201483Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T16:34:53.6306344Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T16:34:53.7103666Z Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest",
            "2026-05-21T16:34:54.8886425Z Successfully installed iniconfig-2.3.0 packaging-26.2 pluggy-1.6.0 pygments-2.20.0 pytest-9.0.3",
            "2026-05-21T16:34:57.4671939Z ##[group]Run python -m pytest -q tests/test_doi_ownership.py",
            "2026-05-21T16:34:57.4672437Z \u001b[36;1mpython -m pytest -q tests/test_doi_ownership.py\u001b[0m",
            "2026-05-21T16:34:58.0003425Z ##[group]Run python -m pytest -q",
            "2026-05-21T16:34:58.0003738Z \u001b[36;1mpython -m pytest -q\u001b[0m",
            "2026-05-21T16:34:58.5021912Z ==================================== ERRORS ====================================",
            "2026-05-21T16:34:58.5022947Z ___ ERROR collecting tests/test_boundary_certificate_against_omnia_limit.py ____",
            "2026-05-21T16:34:58.5024398Z ImportError while importing test module '/home/runner/work/OMNIA/OMNIA/tests/test_boundary_certificate_against_omnia_limit.py'.",
            "2026-05-21T16:34:58.5026511Z Traceback:",
            "2026-05-21T16:34:58.5032146Z E   ModuleNotFoundError: No module named 'omnia_limit'",
            "2026-05-21T16:34:58.5033624Z ERROR tests/test_boundary_certificate_against_omnia_limit.py",
            "2026-05-21T16:34:58.5034370Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T16:34:58.5035019Z 1 error in 0.29s",
            "2026-05-21T16:34:58.5299476Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "2_Python 3.11.txt",
          "lines": [
            "2026-05-21T16:34:49.2196702Z \u001b[36;1mpython -m pip install pytest\u001b[0m",
            "2026-05-21T16:34:50.5377754Z Collecting pytest",
            "2026-05-21T16:34:50.6021749Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T16:34:50.6185263Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T16:34:50.6459638Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T16:34:50.6684725Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T16:34:50.6972949Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T16:34:50.7158986Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T16:34:50.8804173Z Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest",
            "2026-05-21T16:34:51.8541968Z Successfully installed iniconfig-2.3.0 packaging-26.2 pluggy-1.6.0 pygments-2.20.0 pytest-9.0.3",
            "2026-05-21T16:34:54.0495475Z ##[group]Run python -m pytest -q tests/test_doi_ownership.py",
            "2026-05-21T16:34:54.0495935Z \u001b[36;1mpython -m pytest -q tests/test_doi_ownership.py\u001b[0m",
            "2026-05-21T16:34:54.5328090Z ##[group]Run python -m pytest -q",
            "2026-05-21T16:34:54.5328400Z \u001b[36;1mpython -m pytest -q\u001b[0m",
            "2026-05-21T16:34:54.9336089Z ==================================== ERRORS ====================================",
            "2026-05-21T16:34:54.9336857Z ___ ERROR collecting tests/test_boundary_certificate_against_omnia_limit.py ____",
            "2026-05-21T16:34:54.9337572Z ImportError while importing test module '/home/runner/work/OMNIA/OMNIA/tests/test_boundary_certificate_against_omnia_limit.py'.",
            "2026-05-21T16:34:54.9338554Z Traceback:",
            "2026-05-21T16:34:54.9341067Z E   ModuleNotFoundError: No module named 'omnia_limit'",
            "2026-05-21T16:34:54.9341831Z ERROR tests/test_boundary_certificate_against_omnia_limit.py",
            "2026-05-21T16:34:54.9342230Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T16:34:54.9342549Z 1 error in 0.21s",
            "2026-05-21T16:34:54.9573077Z ##[error]Process completed with exit code 2."
          ]
        }
      ]
    }
  ]
}

Patch:
{
  "ci_changed": true,
  "legacy_non_dot_github_removed": [],
  "duplicate_test_workflows_removed": [],
  "python_version_policy": "3.12 only",
  "omnia_required_doi_command_present": true
}

Local tests:
{
  "status": "pass",
  "passed": 57,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "57 passed in 1.85s"
}

Push:
null

After online check:
null

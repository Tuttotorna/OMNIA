# Cyber Risk CVSS — Decision-Validity Case

## Status

This is a real public cyber-risk decision-validity case.

It does not prove OMNIA.

It does not prove new mathematics.

It does not prove novelty in cybersecurity.

It does not define a universal patching policy.

It does not replace exposure-aware vulnerability management.

It does not mean any critical CVE can be ignored.

It shows one specific decision-validity failure:

**CVSS base score alone is the wrong object for this patch-priority decision.**

---

## Definitions

`Omega` = vulnerability field with exploitation / threat-context attributes

`pi` = CVSS base score only

`D` = patch-priority decision using KEV or EPSS threshold as additional context

---

## Policy used for D

This case uses a deliberately explicit test policy:

`URGENT_REMEDIATE_FIRST` if:

- the vulnerability is present in CISA KEV; or
- EPSS >= 0.10

Otherwise:

`STANDARD_CRITICAL_QUEUE` if CVSS >= 9.0

This is not proposed as a universal vulnerability management policy.

It is used only to test whether CVSS alone preserves the distinctions required by this patch-priority decision.

---

## Field data

| cve | cvss_base_score | cvss_severity | cvss_vector | known_exploited_kev | kev_date_added | epss | epss_percentile | epss_date | description | cvss_source | kev_source | epss_source | nvd_error | decision_D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2023-3519 | 9.8 | CRITICAL | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | True | 2023-07-19 | 0.99343 | 0.99933 | 2026-06-15 | Citrix NetScaler ADC and NetScaler Gateway code injection / RCE case; listed by NVD as in CISA KEV. | secure@citrix.com | CISA KEV JSON | FIRST EPSS API |  | URGENT_REMEDIATE_FIRST |
| CVE-2019-17531 | 9.8 | CRITICAL | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | False |  | 0.05329 | 0.91537 | 2026-06-15 | FasterXML jackson-databind polymorphic typing issue; NVD CVSS 9.8. | nvd@nist.gov | CISA KEV JSON not found / fallback | FIRST EPSS API |  | STANDARD_CRITICAL_QUEUE |

---

## Projection pi

| cve | cvss_base_score |
| --- | --- |
| CVE-2023-3519 | 9.8 |
| CVE-2019-17531 | 9.8 |

Result:

`pi(omega_1) = pi(omega_2)` is `True`.

---

## Decision D

| cve | known_exploited_kev | epss | epss_percentile | decision_D |
| --- | --- | --- | --- | --- |
| CVE-2023-3519 | True | 0.99343 | 0.99933 | URGENT_REMEDIATE_FIRST |
| CVE-2019-17531 | False | 0.05329 | 0.91537 | STANDARD_CRITICAL_QUEUE |

Result:

`D(omega_1) = D(omega_2)` is `False`.

---

## Failure condition

The failure condition is:

`pi(omega_1) = pi(omega_2)`

and:

`D(omega_1) != D(omega_2)`

In this case:

`pi(omega_1) = pi(omega_2)` is `True`.

`D(omega_1) != D(omega_2)` is `True`.

Therefore:

`factorization_failure = True`.

---

## Conclusion

Because the same CVSS base score corresponds to two different patch-priority decisions under the stated policy, the decision cannot factor through CVSS base score alone.

So:

`D != d composed with pi`

for any function `d` from CVSS base score alone to this patch-priority decision.

Therefore:

**CVSS base score alone is the wrong object for this patch-priority decision.**

---

## Boundary

This does not mean CVSS is useless.

It means CVSS alone does not preserve the distinctions required by this patch-priority decision.

A real organization must also consider exposure, asset criticality, compensating controls, reachability, exploitability in its own environment, remediation cost, and business impact.

---

## Sources used by the script

- FIRST EPSS API: `https://api.first.org/data/v1/epss`
- CISA KEV JSON: `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`
- NVD CVE API: `https://services.nvd.nist.gov/rest/json/cves/2.0`

---

## Public sentence

Correct answers to the wrong object are not solutions.

---

## Files

- `cyber_risk_field.csv`
- `cvss_projection_pi.csv`
- `patch_priority_decision_D.csv`
- `verdict.json`
- `reproduce.py`

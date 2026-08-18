# Example Output
Illustrative example of what `results_<timestamp>.csv` looks like after running
the script against `topics.txt`. (Generated once locally and pasted here so
visitors can see the shape of the output without needing an API key.)

**Topic:** Automating client onboarding via CRM and webhooks

**Status:** success

**Summary:**

> **Executive Summary:** Manual onboarding steps create delays and inconsistent
> client experiences. Connecting the CRM to key systems via webhooks can
> trigger onboarding tasks automatically as soon as a deal closes.
>
> **Key Actionable Insights:**
> 1. Map every manual onboarding step currently performed after a deal closes.
> 2. Identify which steps can be triggered by a CRM status change (e.g., "Closed Won").
> 3. Set up webhook listeners to fire downstream actions (welcome email, account provisioning, task creation) automatically.
>
> **Recommended Process Workflow:**
> 1. CRM deal status changes to "Closed Won."
> 2. Webhook fires to onboarding service.
> 3. Onboarding service creates account, sends welcome email, and assigns internal owner.
> 4. Status synced back to CRM for visibility.

---

Run `python claude_automation.py` with your own `ANTHROPIC_API_KEY` set to
generate fresh results for the topics in `topics.txt` (or your own file passed
via `--topics`).
